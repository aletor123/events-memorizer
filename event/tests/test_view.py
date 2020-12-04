from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from event.models import Event

from event.factory import EventFactory

from event.forms import EventForm

VIEW_URL = reverse('events:events_list')


class EventTest(TestCase):
    COUNT_OF_EVENTS = 10

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='test_user',
        )
        EventFactory.create_batch(cls.COUNT_OF_EVENTS, owner=cls.user)

    def setUp(self):
        self.client.force_login(self.user)

    def test_view_uses_right_form(self):
        response = self.client.get(VIEW_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].__class__, EventForm)

    def test_view_uses_right_template(self):
        response = self.client.get(VIEW_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events.html')

    def test_create_new_event_ok(self):
        event_data = {
            'title': 'title_test',
            'place': 'place_test',
            'description': 'description_test',
        }
        response = self.client.post(VIEW_URL, event_data)
        self.assertEqual(response.status_code, 302,
                         'Expected Response Code 302, received {0} instead.'.format(response.status_code))

    def _test_form_err(self, event_data, field):
        response = self.client.post(VIEW_URL, event_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', field, 'This field is required.')

    def test_create_new_event_errors(self):
        with self.subTest("test_title"):
            event_data = {
                'title': '',
                'place': 'place_test',
                'description': 'description_test',
            }
            self._test_form_err(event_data, 'title')
        with self.subTest("test_place"):
            event_data = {
                'title': 'title_test',
                'place': '',
                'description': 'description_test',
            }
            self._test_form_err(event_data, 'place')
        with self.subTest("test_description"):
            event_data = {
                'title': 'title_test',
                'place': 'place_test',
                'description': '',
            }
            self._test_form_err(event_data, 'description')

    def test_events_list(self):
        response = self.client.get(VIEW_URL)
        user_events = Event.objects.filter(owner=self.user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['events']), list(user_events))