from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import HomeSettings, WeatherSettings


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        HomeSettings.objects.create(user=instance)
        WeatherSettings.objects.create(user=instance)