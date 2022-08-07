from django import forms
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
