from django.test import TestCase
from world_cup.models import Rider, RaceResult, Team
from django.urls import reverse
from django.utils import timezone



class RiderDetailViewTests(TestCase):
    def setUp(self):
        # Create a Team object first
        self.team = Team.objects.create(name="Enduro Team")

        self.rider = Rider.objects.create(
            first_name="John",
            last_name="Doe",
            age=25,
            team=self.team,  # Associate the team here
            age_category='JNR'
        )

        self.race_result = RaceResult.objects.create(
            rider=self.rider,
            qualifying_time=123.45,
            main_race_time=120.00,
            race_date='2023-01-01'
        )

    def test_rider_detail_view(self):
        # Generate URL using the rider's ID
        url = reverse('rider_details', kwargs={'pk': self.rider.pk})

        # Make the request and capture the response
        response = self.client.get(url)

        # Asserts to check if everything went as expected
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'world_cup/rider_details.html')
        self.assertContains(response, self.rider.first_name)
        self.assertContains(response, self.rider.last_name)
        self.assertContains(response, str(self.race_result.qualifying_time))

class QualifyingResultsViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        team = Team.objects.create(name="Speedsters")
        unique_suffix = timezone.now().strftime("%Y%m%d%H%M%S")
        riders = [
            Rider.objects.create(
                first_name=f"Racer{i}",
                last_name=f"Fast{unique_suffix}{i}",
                age=20 + i,
                team=team,
                age_category='JNR'
            ) for i in range(5)
        ]
        for i, rider in enumerate(riders):
            RaceResult.objects.create(
                rider=rider,
                qualifying_time=120 - i,
                main_race_time=115 - i,
                race_date='2023-01-01'
            )

class RaceOrderViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        team = Team.objects.create(name="Trailblazers")
        unique_suffix = timezone.now().strftime("%Y%m%d%H%M%S")
        riders = [
            Rider.objects.create(
                first_name=f"Rider{i}",
                last_name=f"Quick{unique_suffix}{i}",
                age=20 + i,
                team=team,
                age_category='SNR'
            ) for i in range(5)
        ]
        for i, rider in enumerate(riders):
            RaceResult.objects.create(
                rider=rider,
                qualifying_time=100 + i,
                main_race_time=95 + i,
                race_date='2023-01-01'
            )


class PodiumResultsViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.team = Team.objects.create(name="Champion Team")
        categories = ['U12', 'JNR', 'SNR']
        for cat in categories:
            for i in range(3):  # Three riders per category
                Rider.objects.create(
                    first_name=f"Champion{cat}{i}", last_name=f"Podium{cat}{i}",
                    age=18 + i, team=cls.team, age_category=cat
                )
        for rider in Rider.objects.all():
            RaceResult.objects.create(
                rider=rider,
                qualifying_time=90.0,
                main_race_time=88.0,
                race_date='2023-03-03'
            )

    def test_podium_results(self):
        url = reverse('podium_results')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        for category, results in response.context['categories'].items():
            self.assertEqual(len(results), 3) 

class ListRidersViewTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="AllStar Team")
        Rider.objects.create(first_name="Alice", last_name="Wonderland", age=30, team=self.team, age_category='SNR')

    def test_rider_list_view_filtering(self):
        url = reverse('list_riders')
        response = self.client.get(url, {'search': 'Alice'})
        self.assertContains(response, 'Alice')
        self.assertEqual(len(response.context['riders']), 1)
