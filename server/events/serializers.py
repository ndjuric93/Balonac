from rest_framework.serializers import ModelSerializer, CharField

from events.models import Event, EventPlayer


class EventPlayerSerializer(ModelSerializer):
    player_name = CharField(source='player.name', read_only=True)

    class Meta:
        model = EventPlayer
        fields = ['player_name', 'goals_in_game', 'assists_in_game']


class EventSerializer(ModelSerializer):
    players = EventPlayerSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = (
            'date', 'location', 'score_a', 'score_b', 'players', 'completed'
        )
