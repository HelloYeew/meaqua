from django.contrib import messages
from .forms import UserCreationForms
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views


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
