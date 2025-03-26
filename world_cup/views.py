from django.views import generic
from world_cup.models import Rider, RaceResult
from .forms import RiderForm 
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse

class RiderDetailView(generic.DetailView):
    model = Rider
    template_name = 'world_cup/rider_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rider = self.get_object()
        context['race_results'] = RaceResult.objects.filter(rider=rider).order_by('-race_date')
        return context

class QualifyingResultsView(generic.ListView):
    model = RaceResult
    template_name = 'world_cup/qualifying_results.html'
    context_object_name = 'race_results'

    def get_queryset(self):
        return RaceResult.objects.select_related('rider').order_by('qualifying_time')

class RaceOrderView(generic.ListView):
    model = RaceResult
    template_name = 'world_cup/race_order.html'
    context_object_name = 'race_order'

    def get_queryset(self):
        return RaceResult.objects.select_related('rider').order_by('-qualifying_time')

class PodiumResultsView(generic.TemplateView):
    template_name = 'world_cup/podium_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = {
            category: RaceResult.objects.filter(
                rider__age_category=category[0]
            ).select_related('rider').order_by('main_race_time')[:3]
            for category in Rider.AGE_CATEGORIES
        }
        return context

class RiderCreateView(generic.CreateView):
    model = Rider
    form_class = RiderForm
    template_name = 'world_cup/register_rider.html'

    def get_success_url(self):
        return reverse('list_riders')

class ListRidersView(generic.ListView):
    model = Rider
    template_name = 'world_cup/list_riders.html'
    context_object_name = 'riders'

    def get_queryset(self):
        queryset = Rider.objects.all().select_related('team')
        search_query = self.request.GET.get('search', '')
        age_category_query = self.request.GET.get('age_category', '')

        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) | 
                Q(last_name__icontains=search_query) |
                Q(team__name__icontains=search_query)
            )
        if age_category_query:
            queryset = queryset.filter(age_category=age_category_query)
        return queryset

    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            riders = list(self.get_queryset().values('first_name', 'last_name', 'team__name', 'age_category'))
            return JsonResponse(riders, safe=False)
        else:
            return super().get(request, *args, **kwargs)
