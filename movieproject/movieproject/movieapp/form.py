from django import forms
from . models import movie


class movieform(forms.ModelForm):
    class Meta:
        model=movie
        fields=['img','name','year','des','gen']

