from django import forms
from todos.models import Todos
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


class CreateTodo(forms.ModelForm):

    class Meta:
        model = Todos
        fields = ('title', 'description')

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(CreateTodo, self).__init__(*args, **kwargs)
        # for field in (self.fields['email'], self.fields['password']):
        #     field.widget.attrs.update({'class': 'form-control '})
        self.fields['title'] = forms.CharField(label='Title', error_messages={'required': "Please enter your Title"},
                                               widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Please enter your Title...', 'class': 'form-control', 'autocomplete': 'off', 'oninvalid': "this.setCustomValidity('Please enter your Title')", 'oninput': "this.setCustomValidity('')", 'id': 'create_title'}))
        self.fields['description'] = forms.CharField(label='Description', error_messages={'required': "Please enter your description"},
                                                     widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Please enter your description...', 'class': 'form-control', 'autocomplete': 'off', 'oninvalid': "this.setCustomValidity('Please enter your description')", 'oninput': "this.setCustomValidity('')"}))
