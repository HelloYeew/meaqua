from django.urls import path
from . import views

urlpatterns = [
    path('settings', views.control_panel_home, name='control_panel_home'),
    path('settings/theme/gallery', views.theme_gallery, name='theme_gallery'),
    path('settings/theme/create', views.create_theme, name='create_theme'),
    path('settings/theme/edit/<int:theme_id>', views.edit_theme, name='edit_theme'),
    path('settings/applications/manage', views.manage_applications, name='manage_applications'),
    path('settings/applications/add', views.add_applications, name='add_applications'),
    path('settings/applications/edit/<int:application_id>', views.edit_applications, name='edit_applications'),
    path('settings/applications/delete/<int:application_id>', views.delete_applications, name='delete_applications'),
    path('settings/bookmarks/manage', views.manage_bookmarks, name='manage_bookmarks'),
    path('settings/bookmarks/add', views.add_bookmarks, name='add_bookmarks'),
    path('settings/bookmarks/add_category', views.add_bookmarks_category, name='add_bookmark_category'),
]