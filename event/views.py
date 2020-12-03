from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from .models import Event
from .forms import EventForm


class Events(LoginRequiredMixin, FormMixin, ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events.html'
    success_url = '/events/'
    form_class = EventForm

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            sticker = form.save(commit=False)
            sticker.owner = request.user
            sticker.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_queryset(self):
        return Event.objects.filter(owner=self.request.user)
