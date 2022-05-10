from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.password_validation import validate_password
from django.core import validators

from .models import CustomUser


def username_check(value):
    custom_user_obj = CustomUser.objects.filter(username=value).exists()
    if custom_user_obj:
        raise forms.ValidationError("Username already exsits")


def mobile_check(value):
    if len(str(value)) == 10:
        custom_user_obj = CustomUser.objects.filter(mobile=value).exists()
        if custom_user_obj:
            raise forms.ValidationError("Mobile already used")
    else:
        raise forms.ValidationError("Please enter 10 digit mobile number.")


class CustomUserCreationForm(UserCreationForm):

    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female')])

    # email = forms.CharField(label='Enter email')
    # password1 = forms.CharField(label='Enter password',
    #                             widget = forms.PasswordInput, validators = [validate_password])
    # password2 = forms.CharField(label='Confirm password',
    #                             widget=forms.PasswordInput, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ('username', 'mobile', 'gender',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(label='Username', validators=[username_check], error_messages={'required': "Please enter your username"},
                                                  widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Please enter your username...', 'style': 'width:300px;', 'class': 'form-control', 'oninvalid': "this.setCustomValidity('Please enter your username')", 'oninput': "this.setCustomValidity('')"}))

        self.fields['mobile'] = forms.IntegerField(label='Mobile', validators=[mobile_check], error_messages={'required': "Please enter your mobile"},
                                                   widget=forms.TextInput(attrs={'type': 'number', 'placeholder': 'Please enter your mobile...', 'style': 'width:300px;', 'class': 'form-control', 'oninvalid': "this.setCustomValidity('Please enter your mobile')", 'oninput': "this.setCustomValidity('')"}))

        self.fields['email'] = forms.CharField(label='Email', error_messages={'required': "Please enter your email"},
                                               widget=forms.TextInput(attrs={'type': 'email', 'placeholder': 'Please enter your email...', 'style': 'width:300px;', 'class': 'form-control', 'oninvalid': "this.setCustomValidity('Please enter your email')", 'oninput': "this.setCustomValidity('')"}))

        self.fields['password1'] = forms.CharField(label='Password', error_messages={'required': "Please enter your password"}, validators=[validate_password],
                                                   widget=forms.TextInput(attrs={'placeholder': 'Please enter your password...', 'style': 'width:300px;', 'class': 'form-control', 'type': 'password', 'oninvalid': "this.setCustomValidity('Please enter your password')", 'oninput': "this.setCustomValidity('')"}))
        self.fields['password2'] = forms.CharField(label='Confirm password', error_messages={'required': "Please enter your password"}, validators=[validate_password],
                                                   widget=forms.TextInput(attrs={'placeholder': 'Please enter your password...', 'style': 'width:300px;', 'class': 'form-control', 'type': 'password', 'oninvalid': "this.setCustomValidity('Please enter your password')", 'oninput': "this.setCustomValidity('')"}))

        self.fields['gender'] = forms.ChoiceField(
            label='Gender', choices=[('Male', 'Male'), ('Female', 'Female')])


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
