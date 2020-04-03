from rest_framework.serializers import ModelSerializer

from events.models import Event
from players.serializers import PlayerSerializer


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'date', 'location', 'score_a', 'score_b')


class SingleEventSerializer(ModelSerializer):
    players = EventPlayerSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = (
            'id', 'date', 'location', 'score_a',
            'score_b', 'players', 'completed'
        )
