from django.db import models
from django.contrib.auth.models import User
from theme.models import Theme


class HomeSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_theme = models.ForeignKey(Theme, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username + '\'s home settings'
