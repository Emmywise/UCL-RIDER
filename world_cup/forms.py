from django import forms
from .models import Rider

class RiderForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = ['first_name', 'last_name', 'team', 'age', 'age_category', 'photo'] 
