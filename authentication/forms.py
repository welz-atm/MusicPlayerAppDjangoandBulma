from django import forms
from .admin import UserCreationForm, UserChangeForm
from .models import CustomUser


class UserCreateForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'display_name',)


class UserEditForm(UserChangeForm):
    display_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':
                                                                    'Enter your display name'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'type': 'hidden'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'display_name',)

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''