from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from theme.models import Theme
from .models import HomeSettings


class HomepageSettingsForm(forms.ModelForm):
    current_theme = forms.ModelChoiceField(label='Theme', queryset=Theme.objects.all(), required=False, empty_label='Default')

    class Meta:
        model = HomeSettings
        fields = ['current_theme']

    def __init__(self, *args, **kwargs):
        super(HomepageSettingsForm, self).__init__(*args, **kwargs)
        self.fields['current_theme'].label = 'Change theme'


class UserCreationForms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
