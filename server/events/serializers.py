from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    CharField,
    ListField,
    IntegerField,
    RelatedField
)
from events.models import Event, EventPlayer
from players.serializers import PlayerSerializer
from players.models import Player

from events.services.create import create_event, update_event


class SimpleEventPlayerSerializer(ModelSerializer):
    class Meta:
        model = EventPlayer
        fields = ['player']


class CreateEventSerializer(ModelSerializer):
    event_player = SimpleEventPlayerSerializer(many=True)

    class Meta:
        model = Event
        fields = ['location', 'date', 'event_player']

    def create(self, validated_data):
        event_players = validated_data.pop('event_player')
        event = Event.objects.create(**validated_data)
        for player in event_players:
            EventPlayer.objects.create(event=event, player=player['player'])
        return event


class EventPlayerSerializer(ModelSerializer):
    player_name = CharField(source='player.name', read_only=True)

    class Meta:
        model = EventPlayer
        fields = ['player_name', 'goals_in_game', 'assists_in_game', 'team']


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'date', 'location', 'score_a', 'score_b')


class SingleEventSerializer(ModelSerializer):
    players = EventPlayerSerializer(
        read_only=True, many=True, source='event_player')

    class Meta:
        model = Event
        fields = (
            'date', 'location', 'score_a', 'score_b', 'players', 'completed'
        )
