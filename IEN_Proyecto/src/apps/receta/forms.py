
from django import forms
from .models import Dulce


class RecetaForm1(forms.ModelForm):
    class Meta:
        model = Dulce
        fields = ['nombre', 'tipo',]
