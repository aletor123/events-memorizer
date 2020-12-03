from django import forms

from .models import Event
from .widgets import MapWidget


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'place', 'description')
        widgets = {
            'place': MapWidget(map_attrs={"center": [92.85656693081211, 56.01433428426304],}),
        }
        labels = {
            'place': "Choose event's place",
        }
