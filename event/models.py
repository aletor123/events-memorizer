from django.contrib.auth.models import User
from django.db import models

from django.utils.translation import gettext_lazy as _


# Create your models here.

class Event(models.Model):
    """User event model.

    Attributes:
        owner (Manager): Foreign key User that created this event.
        title (str): Event title.
        place (bool): Location of the event.
        description (set): Event description.

    """
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='own_events',
        verbose_name=_('Owner'),
    )

    title = models.CharField(
        max_length=100,
        verbose_name=_('Title')
    )

    place = models.CharField(
        max_length=250,
        verbose_name=_('Place'),
    )

    description = models.TextField(
        verbose_name=_('Description'),
    )