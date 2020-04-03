from django.contrib import admin
from events.models import Event, EventPlayer
from player.models import Player

admin.site.register(Event)
admin.site.register(EventPlayer)
admin.site.register(Player)
