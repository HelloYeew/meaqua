from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from theme.models import Theme
from users.models import HomeSettings


@login_required
def control_panel_home(request):
    return render(request, 'control_panel/home.html')


def theme_gallery(request):
    # If user logged in, get current_theme
    if request.user.is_authenticated:
        theme_user_setting = HomeSettings.objects.filter(user=request.user).first()
        # If theme is not set, use default theme
        if theme_user_setting.current_theme is None:
            use_default_theme = True
        else:
            use_default_theme = False
        return render(request, 'control_panel/theme/gallery.html', {
            'theme_list': Theme.objects.all(),
            'current_theme': theme_user_setting.current_theme,
            'use_default_theme': use_default_theme
        })
    else:
        return render(request, 'control_panel/theme/gallery.html', {
            'theme_list': Theme.objects.all(),
            'use_default_theme': True
        })
