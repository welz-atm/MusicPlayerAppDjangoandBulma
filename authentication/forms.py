from django import forms
from .admin import UserCreationForm, UserChangeForm
from .models import CustomUser


class UserCreateForm(UserCreationForm):
    display_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':
                                                                    'Enter your display name'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'display_name',)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''


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