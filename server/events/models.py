from django.db import models

from players.models import Player


class Event(models.Model):

    class EventState(models.TextChoices):
        CREATED = 'C'
        PENDING = 'P'
        FINISHED = 'F'

    date = models.DateTimeField()
    location = models.CharField(max_length=32)
    score_a = models.IntegerField(default=0)
    score_b = models.IntegerField(default=0)
    team_a = models.CharField(max_length=32, blank=True, null=True)
    team_b = models.CharField(max_length=32, blank=True, null=True)
    completed = models.CharField(
        max_length=1,
        choices=EventState.choices,
        default=EventState.CREATED)


class EventPlayer(models.Model):
    player = models.ForeignKey(
        Player, related_name='base_player', on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, related_name='event_player', on_delete=models.CASCADE)
    team = models.CharField(max_length=32, blank=True, null=True)
    goals_in_game = models.IntegerField(default=0)
    assists_in_game = models.IntegerField(default=0)
