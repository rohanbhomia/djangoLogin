from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.password_validation import validate_password
from django.core import validators

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    email = forms.CharField(label='Enter email')
    password1 = forms.CharField(label='Enter password',
                                widget=forms.PasswordInput, validators=[validate_password])
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.CharField(label='Enter email',
                                               widget=forms.TextInput(attrs={'type': 'email', 'placeholder': 'Please enter your email...', 'style': 'width:200px;'}))
        self.fields['password1'] = forms.CharField(label='Enter password', validators=[validate_password],
                                                   widget=forms.TextInput(attrs={'placeholder': 'Please enter your password...', 'style': 'width:200px;'}))
        self.fields['password2'] = forms.CharField(label='Confirm password', validators=[validate_password],
                                                   widget=forms.TextInput(attrs={'placeholder': 'Please enter your password...', 'style': 'width:200px;'}))


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
