from django.db import models
from mezzanine.core.fields import RichTextField
from mezzanine.pages.models import Page


class Event(Page):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    content = RichTextField(blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    guestlist = models.IntegerField()

    class Meta:
        verbose_name = u'Event'
        verbose_name_plural = u'Events'
