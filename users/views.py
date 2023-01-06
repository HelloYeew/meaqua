from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserCreationForms, WeatherSettingsForm, HomepageSettingsForm
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views

from .models import WeatherSettings, HomeSettings


class LogoutAndRedirect(auth_views.LogoutView):
    # Redirect to / after logout
    def get_next_page(self):
        return '/'


def signup(request):
    if request.method == 'POST':
        form = UserCreationForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}! Now you can login.')
            return redirect('login')
    else:
        form = UserCreationForms()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def settings(request):
    theme_user_setting = HomeSettings.objects.filter(user=request.user).first()
    # If theme is not set, use default theme
    if theme_user_setting.current_theme is None:
        use_default_theme = True
    else:
        use_default_theme = False
    if request.method == 'POST':
        weather_form = WeatherSettingsForm(request.POST)
        home_form = HomepageSettingsForm(request.POST)
        if weather_form.is_valid() and home_form.is_valid():
            weather_setting = weather_form.save(commit=False)
            weather_setting_object = WeatherSettings.objects.get(user=request.user)
            weather_setting_object.city = weather_setting.city
            weather_setting_object.save()
            home_setting = home_form.save(commit=False)
            home_setting_object = HomeSettings.objects.get(user=request.user)
            home_setting_object.current_theme = home_setting.current_theme
            home_setting_object.auto_play_video = home_setting.auto_play_video
            home_setting_object.mute_video = home_setting.mute_video
            home_setting_object.save()
            messages.success(request, 'Settings saved successfully!')
    else:
        weather_form = WeatherSettingsForm(instance=WeatherSettings.objects.get(user=request.user))
        home_form = HomepageSettingsForm(instance=HomeSettings.objects.get(user=request.user))
    return render(request, 'users/settings.html', {
        'weather_form': weather_form,
        'home_form': home_form,
        'current_theme': theme_user_setting.current_theme,
        'use_default_theme': use_default_theme
    })
