from django.db import models

from players.models import Player


class EventPlayer(Player):
    player = models.ForeignKey(
        Player, related_name='base_player', on_delete=models.CASCADE)
    team = models.CharField(max_length=32, blank=True, null=True)


class Event(models.Model):
    date = models.DateTimeField()
    location = models.CharField(max_length=32)
    players = models.ManyToManyField(EventPlayer, blank=True)
    score_a = models.IntegerField(default=0)
    score_b = models.IntegerField(default=0)
    team_a = models.CharField(max_length=32, blank=True, null=True)
    team_b = models.CharField(max_length=32, blank=True, null=True)
    completed = models.BooleanField(default=False)
