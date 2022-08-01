from django.shortcuts import render
from users.models import HomeSettings
from theme.models import Application, BookmarkCategory, Bookmark


def home(request):
    if request.user.is_authenticated:
        theme_user_setting = HomeSettings.objects.filter(user=request.user).first()
        bookmark_category_list = BookmarkCategory.objects.filter(user=request.user)
        # Create a list of bookmark categories name
        bookmark_category_name_list = []
        for bookmark_category in bookmark_category_list:
            bookmark_category_name_list.append(bookmark_category.name)
        bookmark_list = Bookmark.objects.filter(user=request.user)
        # If theme is not set, use default theme
        use_default_theme = False
        if theme_user_setting.current_theme is None:
            use_default_theme = True
        return render(request, 'index.html', {
            'use_default_theme': use_default_theme,
            'theme': theme_user_setting.current_theme,
            'applications': Application.objects.filter(user=request.user),
            'bookmark_name_list': bookmark_category_name_list,
            'bookmark_list': bookmark_list
        })
    else:
        return render(request, 'index.html', {'use_default_theme': True})
