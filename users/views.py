from django.shortcuts import render
from django.contrib.auth import views as auth_views


class LogoutAndRedirect(auth_views.LogoutView):
    # Redirect to / after logout
    def get_next_page(self):
        return '/'
