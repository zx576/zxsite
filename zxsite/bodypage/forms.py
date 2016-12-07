from django import forms

class Portrait(forms.Form):
    porfile = forms.ImageField()