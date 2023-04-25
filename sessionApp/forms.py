from django import forms 
from django.core import validators

class ItemsForm(forms.Form):
    item = forms.CharField(max_length=30)
    quantity = forms.IntegerField(widget=forms.Select(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)]))
