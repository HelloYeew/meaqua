from django.urls import path
from . import views

urlpatterns = [
    path('settings', views.control_panel_home, name='control_panel_home'),
    path('theme/gallery', views.theme_gallery, name='theme_gallery'),
]