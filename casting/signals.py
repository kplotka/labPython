from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from casting.models import ModelProfile

@receiver(post_save, sender=User)
def create_default_model_profile(sender, instance, created, **kwargs):
    if created:
        # Tworzymy domyślnie ModelProfile z pełną nazwą ustawioną na username
        ModelProfile.objects.create(user=instance, full_name=instance.username)