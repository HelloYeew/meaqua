from django import forms
from django.core.validators import FileExtensionValidator

from theme.models import Theme, Video, Application


class CreateNewThemeForm(forms.ModelForm):
    name = forms.CharField(label="Theme name", help_text="A theme name", max_length=255)
    title = forms.CharField(label="Theme title", help_text="A title of your theme that will show on the browser's tab", max_length=255)
    background = forms.ImageField(label="Background Image", help_text="A cool background images.", validators=[FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])])
    favicon = forms.ImageField(label="Favicon", help_text="A favicon that will show on browser's tab. This required PNG file.", validators=[FileExtensionValidator(allowed_extensions=['png'])], required=False)
    color_primary = forms.CharField(label="Primary color", widget=forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}), help_text="A primary color of your theme. This mainly use as text color.", max_length=255, initial='#DFD9D6')
    color_accent = forms.CharField(label="Accent color", widget=forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}), help_text="An accent color of your theme. This color will be use as the theme's second color.", max_length=255, initial='#DBC2D1')
    color_background = forms.CharField(label="Background color", widget=forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}), help_text="A background color of your theme. This color will be use anywhere on background element.", max_length=255, initial='#0A0A0A')
    mask_opacity = forms.FloatField(label="Mask Opacity", help_text="A mask opacity of the mask between theme's body and background", max_value=1, min_value=0, initial=0.5)
    video = forms.ModelChoiceField(label="Video", help_text="Set your background as a cool video. The background image will show instead if the video is not set.", queryset=Video.objects.all(), required=False, empty_label='No video')
    welcome_text = forms.CharField(max_length=255, required=False, help_text="A welcome text that will show to make your day.")

    class Meta:
        model = Theme
        fields = ['name', 'title', 'background', 'favicon', 'color_primary', 'color_accent', 'color_background', 'mask_opacity', 'video', 'welcome_text']


class AddApplicationsForm(forms.ModelForm):
    name = forms.CharField(label="Application name", help_text="An applications name", max_length=255)
    description = forms.CharField(label="Description", help_text="A short explanation of this application. If this is blank, it will show the application's URL instead", max_length=255)
    url = forms.URLField(label="URL", help_text="An applications URL", max_length=255)
    icon_name = forms.CharField(label="Icon name", help_text="A material icon name from materialdesignicons.com", max_length=255)

    class Meta:
        model = Application
        fields = ['name', 'description', 'url', 'icon_name']