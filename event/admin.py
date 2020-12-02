from django import forms
from django.contrib import admin

# Register your models here.
from .forms import EventForm
from .models import Event
from easy_maps.models import Address


class EventAdmin(admin.ModelAdmin):
    form = EventForm


admin.site.register(Event, EventAdmin)
admin.site.register(Address)