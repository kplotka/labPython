from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CastingOffer, Application, ModelProfile, DirectorProfile

ROLE_CHOICES = [
    ('model', 'Model/Modelka'),
    ('director', 'Casting Director'),
]

class CastingOfferForm(forms.ModelForm):
    class Meta:
        model = CastingOffer
        fields = ['title', 'description', 'requirements', 'offer_date', 'location']
        widgets = {'offer_date': forms.DateInput(attrs={'type': 'date'})}

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['message']

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=ROLE_CHOICES, label="Rola")
    class Meta:
        model = User
        fields = ("username", "email", "role", "password1", "password2")

class ModelProfileForm(forms.ModelForm):
    class Meta:
        model = ModelProfile
        fields = ['full_name', 'age', 'height', 'weight', 'measurements', 'portfolio_url', 'profile_picture', 'bio']

class DirectorProfileForm(forms.ModelForm):
    class Meta:
        model = DirectorProfile
        fields = ['full_name', 'agency_name', 'agency_address', 'bio', 'profile_picture']