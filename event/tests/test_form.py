from django.test import TestCase

from event.forms import EventForm

from event.widgets import MapWidget


class EventFormTest(TestCase):
    def test_map_widget_at_place_field_in_form(self):
        form = EventForm
        self.assertEqual(form.Meta.widgets['point'].__class__, MapWidget)
