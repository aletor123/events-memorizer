from django import forms
from easy_maps.widgets import AddressWithMapWidget

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'place', 'description')
        widgets = {
            'place': AddressWithMapWidget({'class': 'vTextField'})
        }
