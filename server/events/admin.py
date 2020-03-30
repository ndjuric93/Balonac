from django.contrib import admin
from player.models import Player
from events.models import Event

# Register your models here.
admin.site.register(Player)
admin.site.register(Event)
