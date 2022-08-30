from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from control_panel.forms import CreateNewThemeForm, AddApplicationsForm
from theme.models import Theme, Application, Bookmark, BookmarkCategory
from users.models import HomeSettings


@login_required
def control_panel_home(request):
    # TODO: If settings homepage complete, remove this line
    return redirect('theme_gallery')


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


@login_required
def create_theme(request):
    theme_user_setting = HomeSettings.objects.filter(user=request.user).first()
    # If theme is not set, use default theme
    if theme_user_setting.current_theme is None:
        use_default_theme = True
    else:
        use_default_theme = False
    if request.method == 'POST':
        create_form = CreateNewThemeForm(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.instance.user = request.user
            create_form.save()
            # Set user's current_theme to this theme
            theme_user_setting.current_theme = create_form.instance
            theme_user_setting.save()
            messages.success(request, 'Theme created successfully!')
            return redirect('theme_gallery')
    else:
        create_form = CreateNewThemeForm()
    return render(request, 'control_panel/theme/create.html', {
        'create_form': create_form,
        'current_theme': theme_user_setting.current_theme,
        'use_default_theme': use_default_theme
    })


@login_required
def manage_applications(request):
    theme_user_setting = HomeSettings.objects.filter(user=request.user).first()
    # If theme is not set, use default theme
    if theme_user_setting.current_theme is None:
        use_default_theme = True
    else:
        use_default_theme = False
    return render(request, 'control_panel/application/manage.html', {
        'current_theme': theme_user_setting.current_theme,
        'use_default_theme': use_default_theme,
        'applications': Application.objects.filter(user=request.user)
    })


@login_required
def add_applications(request):
    theme_user_setting = HomeSettings.objects.filter(user=request.user).first()
    # If theme is not set, use default theme
    if theme_user_setting.current_theme is None:
        use_default_theme = True
    else:
        use_default_theme = False
    if request.method == 'POST':
        add_form = AddApplicationsForm(request.POST)
        if add_form.is_valid():
            add_form.instance.user = request.user
            add_form.save()
            messages.success(request, 'Application added successfully!')
            return redirect('manage_applications')
    else:
        add_form = AddApplicationsForm()
    return render(request, 'control_panel/application/add.html', {
        'add_form': add_form,
        'current_theme': theme_user_setting.current_theme,
        'use_default_theme': use_default_theme
    })


@login_required
def manage_bookmarks(request):
    theme_user_setting = HomeSettings.objects.filter(user=request.user).first()
    # If theme is not set, use default theme
    if theme_user_setting.current_theme is None:
        use_default_theme = True
    else:
        use_default_theme = False
    bookmark_category_list = BookmarkCategory.objects.filter(user=request.user)
    bookmark_category_name_list = []
    for bookmark_category in bookmark_category_list:
        bookmark_category_name_list.append(bookmark_category.name)
    bookmark_list = Bookmark.objects.filter(user=request.user)
    return render(request, 'control_panel/bookmark/manage.html', {
        'current_theme': theme_user_setting.current_theme,
        'use_default_theme': use_default_theme,
        'bookmark_name_list': bookmark_category_name_list,
        'bookmark_list': bookmark_list,
    })
