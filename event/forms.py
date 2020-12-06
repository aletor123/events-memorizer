from django import forms

from .models import Event
from .widgets import MapWidget, AdminMapWidget


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'point', 'place', 'description')
        widgets = {
            'point': MapWidget(map_attrs={"center": [92.85656693081211, 56.01433428426304], }),
        }
        labels = {
            'point': "Choose event's place",
        }


class AdminEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('owner', 'title', 'point', 'place', 'description')
        widgets = {
            'point': AdminMapWidget(map_attrs={"center": [92.85656693081211, 56.01433428426304], }),
        }
        labels = {
            'point': "Choose event's place",
        }
