from django.db import models
from django.urls import reverse

class Rider(models.Model):
    """
    Represents a single UCI Enduro Rider.
    """
    AGE_CATEGORIES = (
        ('U12', 'Under 12'),
        ('JNR', 'Junior'),
        ('SNR', 'Senior'),
    )
    first_name = models.CharField(
        max_length=20,
        unique=True,
        help_text="Rider's First name",
    )
    last_name = models.CharField(
        max_length=20,
        unique=True,
        help_text="Rider's Surname",
    )
    team = models.ForeignKey(
        "Team", on_delete=models.PROTECT,
        help_text='Team the Rider races for',
    )
    age = models.PositiveIntegerField(
        help_text="Rider's age in years."
    )
    age_category = models.CharField(max_length=20, choices=AGE_CATEGORIES, help_text="Age category of the rider")

    photo = models.ImageField(
        upload_to='rider_photos/', blank=True, null=True
    )

    class Meta:
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.age_category})"

    def get_absolute_url(self):
        return reverse('rider_details', kwargs={'pk': self.pk})
    

class RaceResult(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='results')
    qualifying_time = models.FloatField()
    main_race_time = models.FloatField(null=True, blank=True) 
    race_date = models.DateField()

    class Meta:
        ordering = ['qualifying_time'] 
    def __str__(self):
        return f"{self.rider} - Qualifying Time: {self.qualifying_time}"


class Team(models.Model):
    """
    Represents a single UCI Enduro Team.
    """
    name = models.CharField(
        max_length=25,
        unique=True,
        help_text="Name of the team",
    )

    def __str__(self):
        return self.name

