from django.shortcuts import render
from users.models import HomeSettings


def home(request):
    if request.user.is_authenticated:
        theme = HomeSettings.objects.filter(user=request.user).first().current_theme
        # If theme is not set, use default theme
        if theme is None:
            return render(request, 'index.html', {'use_default_theme': True})
        else:
            return render(request, 'index.html', {'theme': theme})
    else:
        return render(request, 'index.html', {'use_default_theme': True})
