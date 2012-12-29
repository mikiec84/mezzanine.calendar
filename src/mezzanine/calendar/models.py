from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    guestlist = models.IntegerField()
