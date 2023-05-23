from django import forms
from mapbox_location_field.forms import LocationField
from django.core.validators import MinLengthValidator

from .models import Place


class MemoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, validators=[MinLengthValidator(3)], required=True)
    comment = forms.CharField(widget=forms.Textarea, required=True)
    location = forms.CharField(required=True)

    class Meta:
        model = Place
        fields = ['name', 'comment', 'location']
        labels = {
            'name': 'Place name:',
            'comment': 'Description for this place:'
        }
