from django.db import models
from django.contrib.auth.models import User

class ModelProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='model_profile')
    full_name = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True, help_text="W cm")
    weight = models.PositiveIntegerField(null=True, blank=True, help_text="W kg")
    measurements = models.CharField(max_length=50, blank=True, help_text="Np. 90-60-90")
    portfolio_url = models.URLField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='models/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.full_name or self.user.username

class DirectorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='director_profile')
    full_name = models.CharField(max_length=100, blank=True)
    agency_name = models.CharField(max_length=200, blank=True)
    agency_address = models.CharField(max_length=200, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='directors/', blank=True, null=True)

    def __str__(self):
        return self.full_name or self.user.username

class CastingOffer(models.Model):
    director = models.ForeignKey(DirectorProfile, on_delete=models.CASCADE, related_name='casting_offers', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    offer_date = models.DateField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    offer = models.ForeignKey(CastingOffer, on_delete=models.CASCADE, related_name='applications')
    model_profile = models.ForeignKey(ModelProfile, on_delete=models.CASCADE, related_name='applications')
    message = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Oczekujące")

    def __str__(self):
        return f"Aplikacja {self.id} dla oferty {self.offer.title} przez {self.model_profile.full_name}"