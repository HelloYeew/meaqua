from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
from django.core.validators import FileExtensionValidator


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'ogg'])])
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name + ' by ' + self.user.username


class Theme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    background = models.ImageField(upload_to='backgrounds/', validators=[FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])])
    favicon = models.ImageField(upload_to='favicon/', validators=[FileExtensionValidator(allowed_extensions=['png'])], blank=True)
    color_primary = ColorField(default='#DFD9D6')
    color_accent = ColorField(default='#DBC2D1')
    color_background = ColorField(default='#0A0A0A')
    mask_opacity = models.FloatField(default=0.5, max_length=1)
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True, blank=True)
    welcome_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name + ' by ' + self.user.username


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=255)
    icon_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name + ' by ' + self.user.username


class BookmarkCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name + ' by ' + self.user.username


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    icon_name = models.CharField(max_length=255)
    category = models.ForeignKey(BookmarkCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' (' + self.category.name + ')' + ' by ' + self.user.username
