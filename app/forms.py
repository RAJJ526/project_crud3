from django import forms
from .models import *
class Registerform(forms.ModelForm):
    class Meta:
        model=Register
        fields="__all__"

