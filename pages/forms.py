from django import forms
from django.db import models
from django.db.models import fields
from .models import UserName

# Method 1 for form POST method
# Method 1 is similar to method 2 and easy as compare to other methods
class SigninForm(forms.ModelForm):
    name      = forms.CharField( label='Username',
                                 required=True, 
                                 widget=forms.TextInput(
                                     attrs={
                                         'placeholder': 'example123',
                                }))
    email     = forms.EmailField( label='Email',
                                  required=False,
                                )
    password  = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    'placeholder' : 'dsaJLkh@jgh897'
                                }),
                                required=True
                                )

    class Meta:
        model = UserName
        fields = [
            'name',
            'email',
            'password'
        ]
    
    # Validating form data 
    # clean_<field_name>
    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        if 'geek' not in name:
            raise forms.ValidationError("Username should contain geek")
        return name


#Method 2 for Form PoST method
class SignInForm2(forms.Form):
    name      = forms.CharField( label='Username',
                                 required=True, 
                                 widget=forms.TextInput(
                                     attrs={
                                         'placeholder': 'example123',
                                }))
    email     = forms.EmailField( label='Email',
                                  required=False,
                                )
    password  = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    'placeholder' : 'dsaJLkh@jgh897'
                                }),
                                required=True
                                )