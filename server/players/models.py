from django.db import models
from django.contrib.auth import get_user_model


class Player(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    appearances = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
