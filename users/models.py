from django.db import models
from django.contrib.auth.models import User
from theme.models import Theme


class HomeSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_theme = models.ForeignKey(Theme, on_delete=models.CASCADE, null=True, blank=True)
    auto_play_video = models.BooleanField(default=True)
    mute_video = models.BooleanField(default=False)
    video_volume = models.FloatField(default=1)

    def __str__(self):
        return self.user.username + '\'s home settings'


class WeatherSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username + '\'s weather settings'
