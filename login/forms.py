from django import forms
from users.models import CustomUser
from django.contrib.auth import authenticate


class AccountAuthenticationForm(forms.ModelForm):
    """
      Form for Logging in  users
    """
    #password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email...', 'style': 'width:240px;'}),

        }

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(AccountAuthenticationForm, self).__init__(*args, **kwargs)
        # for field in (self.fields['email'], self.fields['password']):
        #     field.widget.attrs.update({'class': 'form-control '})
        self.fields['email'] = forms.CharField(label='Email',
                                               widget=forms.TextInput(attrs={'type': 'email', 'placeholder': 'Please enter your email...', 'class': 'form-control', 'autocomplete': 'off'}))
        self.fields['password'] = forms.CharField(label='Password',
                                                  widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Please enter your password...', 'class': 'form-control', 'autocomplete': 'off'}))

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')
