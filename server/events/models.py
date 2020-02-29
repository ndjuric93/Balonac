from django.db import models

from players.models import Player


class Event(models.Model):
    date = models.DateTimeField()
    location = models.CharField(max_length=32)
    players = models.ManyToManyField(Player, blank=True)
