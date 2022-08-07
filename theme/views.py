from django.shortcuts import render
from users.models import HomeSettings
from theme.models import Application, BookmarkCategory, Bookmark, Theme
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
                theme_user_setting.save()
                # add message to indicate theme change
                messages.success(request, 'Theme changed successfully!')
        else:
            settings_form = HomepageSettingsForm(initial={'current_theme': theme_user_setting.current_theme})
        # If theme is not set, use default theme
        if theme_user_setting.current_theme is None:
            use_default_theme = True
        return render(request, 'index.html', {
            'use_default_theme': use_default_theme,
            'theme': theme_user_setting.current_theme,
            'applications': Application.objects.filter(user=request.user),
            'bookmark_name_list': bookmark_category_name_list,
            'bookmark_list': bookmark_list,
            'settings': settings_form
        })
    else:
        return render(request, 'index.html', {'use_default_theme': True})


def theme_gallery(request):
    # If user logged in, get current_theme
    if request.user.is_authenticated:
        theme_user_setting = HomeSettings.objects.filter(user=request.user).first()
        # If theme is not set, use default theme
        if theme_user_setting.current_theme is None:
            use_default_theme = True
        else:
            use_default_theme = False
        return render(request, 'theme/gallery.html', {
            'theme_list': Theme.objects.all(),
            'current_theme': theme_user_setting.current_theme,
            'use_default_theme': use_default_theme
        })
    else:
        return render(request, 'theme/gallery.html', {
            'theme_list': Theme.objects.all(),
            'use_default_theme': True
        })

