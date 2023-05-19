from django import forms
from .models import Place


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'comment']
