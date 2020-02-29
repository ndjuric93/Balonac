from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=32)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    appearances = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
