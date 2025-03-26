from django.urls import path
from .views import ListRidersView, QualifyingResultsView, RaceOrderView, RiderDetailView, RiderCreateView, PodiumResultsView


from world_cup.views import ListRidersView

urlpatterns = [
    path('riders/', ListRidersView.as_view(), name='list_riders'),
    path('riders/<int:pk>/', RiderDetailView.as_view(), name='rider_details'),
    path('qualifying/', QualifyingResultsView.as_view(), name='qualifying_results'),
    path('race_order/', RaceOrderView.as_view(), name='race_order'),
    path('register/', RiderCreateView.as_view(), name='register_rider'),
    path('podium/', PodiumResultsView.as_view(), name='podium_results'),
]
