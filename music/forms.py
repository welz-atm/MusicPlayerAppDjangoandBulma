from django import forms
from .models import Track


class TrackForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'control', 'placeholder':
                                                                    'Enter your display name'}))
    song = forms.FileField(label='', widget=forms.FileInput(attrs={'class': 'control', 'placeholder':
                                                                   'Enter your display name'}))

    class Meta:
        model = Track
        fields = ('title', 'song', )