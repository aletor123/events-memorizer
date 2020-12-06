from django import forms
from django.contrib import admin

# Register your models here.

from .forms import AdminEventForm
from .models import Event
from mapbox_location_field.admin import MapAdmin


class EventAdmin(MapAdmin):
    form = AdminEventForm


admin.site.register(Event, EventAdmin)
