from django import forms
from django.db import models
from django.db.models import fields
from .models import Article

class ArticleForm(forms.ModelForm):
    title    = forms.CharField(required=True,
                               label= "Title",  
                               widget=forms.TextInput(
                                      attrs={
                                        "placeholder":"Human Rights",
                                            }))
    topic    = forms.CharField(required=True,
                               label = "Topic",
                               widget = forms.TextInput(
                                          attrs={
                                              "placeholder": "Human Rights"
                                          }
                               ))
    words    = forms.IntegerField(required=True,
                                label= "Words",
                                widget = forms.NumberInput(
                                          attrs={
                                              "placeholder": 300
                                          }))

    class Meta:
        model  = Article
        fields  = [
            'title',
            'topic',
            'words'
        ]

