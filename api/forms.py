from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Questions
from datetime import datetime

SORTING_CHOICES = ( 
    ("activity", "activity"), 
    ("creation", "creation"), 
    ("votes", "votes"), 
    ("relevance", "relevance"), 
    )
ORDER_CHOICES = ( 
    ("asc", "asc"), 
    ("desc", "desc"), 
    )

class QueryForm(forms.ModelForm):
    age = forms.IntegerField(required = False)
    pagesize= forms.IntegerField(required = False)
    fromdate= forms.DateField(required = False,widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    todate= forms.DateField(initial=datetime.now().strftime("%Y-%m-%d"),required = False,widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    order= forms.ChoiceField(choices=ORDER_CHOICES,required = False)
    min= forms.DateField(required = False,widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    max= forms.DateField(required = False,widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    sort= forms.ChoiceField(choices=SORTING_CHOICES, required = False)
    q= forms.CharField(empty_value = None,required = False)
    accepted= forms.BooleanField(required = False)
    answers= forms.IntegerField(required = False)
    body= forms.CharField(empty_value = None,required = False)
    closed= forms.BooleanField(required = False)
    migrated= forms.BooleanField(required = False)
    notice= forms.BooleanField(required = False)
    nottagged= forms.CharField(empty_value = None,required = False)
    tagged= forms.CharField(empty_value = None,required = False)
    title= forms.CharField(empty_value = None,required = False)
    user= forms.IntegerField(required = False)
    url= forms.CharField(empty_value = None,required = False)
    views= forms.IntegerField(required = False)
    wiki= forms.BooleanField(required = False)
    site= "stackoverflow"

    class Meta:
        model=Questions
        fields='__all__'