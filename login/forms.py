from django import forms
from users.models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


class AccountAuthenticationForm(forms.ModelForm):
    """
      Form for Logging in  users
    """
    #password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        # widgets = {
        #     'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email...', 'style': 'width:240px;'}),

        # }

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(AccountAuthenticationForm, self).__init__(*args, **kwargs)
        # for field in (self.fields['email'], self.fields['password']):
        #     field.widget.attrs.update({'class': 'form-control '})
        self.fields['email'] = forms.CharField(label='Email', error_messages={'required': "Please enter your email"},
                                               widget=forms.TextInput(attrs={'type': 'email', 'placeholder': 'Please enter your email...', 'class': 'form-control', 'autocomplete': 'off', 'oninvalid': "this.setCustomValidity('Please enter your email')", 'oninput': "this.setCustomValidity('')"}))
        self.fields['password'] = forms.CharField(label='Password', error_messages={'required': "Please enter your password"},
                                                  widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Please enter your password...', 'class': 'form-control', 'autocomplete': 'off', 'oninvalid': "this.setCustomValidity('Please enter your password')", 'oninput': "this.setCustomValidity('')"}))

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')


class ChangePassword(forms.Form):

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(ChangePassword, self).__init__(*args, **kwargs)

        self.fields['password1'] = forms.CharField(label='New password', error_messages={'required': "Please enter your password"}, validators=[validate_password],
                                                   widget=forms.TextInput(attrs={'placeholder': 'Please enter your password...', 'style': 'width:300px;', 'class': 'form-control', 'type': 'password', 'oninvalid': "this.setCustomValidity('Please enter your password')", 'oninput': "this.setCustomValidity('')"}))
        self.fields['password2'] = forms.CharField(label='Confirm password', error_messages={'required': "Please enter your password"}, validators=[validate_password],
                                                   widget=forms.TextInput(attrs={'placeholder': 'Please enter your password...', 'style': 'width:300px;', 'class': 'form-control', 'type': 'password', 'oninvalid': "this.setCustomValidity('Please enter your password')", 'oninput': "this.setCustomValidity('')"}))

    def clean(self):
        if self.is_valid():

            password = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')

            if password != password2:
                raise forms.ValidationError(
                    'Both new password and confirm password should be same')
