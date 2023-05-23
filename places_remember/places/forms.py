from django import forms
from mapbox_location_field.forms import LocationField
from django.core.validators import MinLengthValidator

from .models import Place


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'comment', 'location']
        labels = {
            'name': 'Place name:',
            'comment': 'Description for this place:'
        }
