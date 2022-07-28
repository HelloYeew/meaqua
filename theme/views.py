from django.shortcuts import render
from users.models import HomeSettings
from theme.models import Application

def home(request):
    # Get login form from django.contrib.auth.forms

    if request.user.is_authenticated:
        theme_user_setting = HomeSettings.objects.filter(user=request.user).first()
        # If theme is not set, use default theme
        if theme_user_setting is None:
            return render(request, 'index.html', {'use_default_theme': True})
        else:
            return render(request, 'index.html', {
                'use_default_theme': False,
                'theme': theme_user_setting.current_theme,
                'applications': Application.objects.filter(user=request.user)
            })
    else:
        return render(request, 'index.html', {'use_default_theme': True})
