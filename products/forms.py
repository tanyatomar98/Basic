from django import forms
from django.db import models
from django.db.models import fields
from django.forms.widgets import TextInput
from .models import Products


class ProductsForm(forms.ModelForm):
    title = forms.CharField(widget=TextInput(attrs={"placeholder":"Enter your title"}))

    class Meta:
        model = Products
        fields = [
            'title'
        ]
        
