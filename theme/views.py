from django.shortcuts import render
from users.models import HomeSettings, WeatherSettings
from theme.models import Application, BookmarkCategory, Bookmark
from django.contrib import messages
from users.forms import HomepageSettingsForm


def home(request):
    if request.user.is_authenticated:
        theme_user_setting = HomeSettings.objects.filter(user=request.user).first()
        bookmark_category_list = BookmarkCategory.objects.filter(user=request.user)
        # Create a list of bookmark categories name
        bookmark_category_name_list = []
        for bookmark_category in bookmark_category_list:
            bookmark_category_name_list.append(bookmark_category.name)
        bookmark_list = Bookmark.objects.filter(user=request.user)
        use_default_theme = False
        if request.method == 'POST':
            settings_form = HomepageSettingsForm(request.POST)
            if settings_form.is_valid():
                theme_user_setting.current_theme = settings_form.cleaned_data['current_theme']
                theme_user_setting.auto_play_video = settings_form.cleaned_data['auto_play_video']
                theme_user_setting.mute_video = settings_form.cleaned_data['mute_video']
                theme_user_setting.save()
                # add message to indicate theme change
                messages.success(request, 'Settings updated successfully!')
        else:
            settings_form = HomepageSettingsForm(instance=theme_user_setting)
        # If theme is not set, use default theme
        if theme_user_setting.current_theme is None:
            use_default_theme = True
        return render(request, 'index.html', {
            'use_default_theme': use_default_theme,
            'theme': theme_user_setting.current_theme,
            'auto_play_video': theme_user_setting.auto_play_video,
            'mute_video': theme_user_setting.mute_video,
            'applications': Application.objects.filter(user=request.user),
            'bookmark_name_list': bookmark_category_name_list,
            'bookmark_list': bookmark_list,
            'settings': settings_form,
            # TODO: Self-rendered weather using JSON wttr.in/Bangkok?format=j1
            'weather_setting': WeatherSettings.objects.filter(user=request.user).first()
        })
    else:
        return render(request, 'index.html', {'use_default_theme': True})
