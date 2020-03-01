from rest_framework.serializers import ModelSerializer

from events.models import Event
from players.serializers import PlayerSerializer


class EventSerializer(ModelSerializer):
    players = PlayerSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = ('date', 'location', 'players', 'completed')
