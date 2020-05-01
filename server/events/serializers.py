from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    CharField,
    ListField,
    IntegerField,
    DateTimeField,
    RelatedField,
    PrimaryKeyRelatedField,
    ValidationError
)
from events.models import Event, EventPlayer
from players.serializers import PlayerSerializer
from players.models import Player

from events.services.create import create_event, update_event


class SimpleEventPlayerSerializer(ModelSerializer):
    class Meta:
        model = EventPlayer
        fields = ['id', 'player', 'team']


class CreateEventSerializer(ModelSerializer):
    event_player = SimpleEventPlayerSerializer(many=True)
    date = DateTimeField(format='%Y-%m-%d %H:%M', required=True)

    class Meta:
        model = Event
        fields = ['id', 'location', 'date', 'event_player', 'completed']

    def create(self, validated_data):
        event_players = validated_data.pop('event_player')
        return create_event(
            event_data=validated_data,
            event_players=event_players
        )


class UpdateEventSerializer(ModelSerializer):
    event_player = SimpleEventPlayerSerializer(many=True)
    date = DateTimeField(format='%Y-%m-%d %H:%M:%s', required=True)

    class Meta:
        model = Event
        fields = ['location', 'date', 'event_player', 'completed']

    def update(self, instance, validated_data):
        if instance.completed != Event.EventState.CREATED:
            raise ValidationError('Event must be in CREATED state')
        event_players = validated_data.pop('event_player')
        return update_event(
            event=instance,
            event_data=validated_data,
            event_players=event_players
        )


class EventPlayerSerializer(ModelSerializer):
    player_name = CharField(source='player.name', read_only=True)
    player_id = CharField(source='player.id', read_only=True)

    class Meta:
        model = EventPlayer
        fields = ['id', 'player_name', 'player_id', 'goals_in_game', 'assists_in_game', 'team']


class EventSerializer(ModelSerializer):
    date = DateTimeField(format='%B %d, %H:%M')

    class Meta:
        model = Event
        fields = ('id', 'date', 'location', 'score_a', 'score_b', 'completed')


class SingleEventSerializer(ModelSerializer):
    players = EventPlayerSerializer(
        read_only=True, many=True, source='event_player')
    date = DateTimeField(format='%B %d, %H:%M')

    class Meta:
        model = Event
        fields = (
            'date', 'location', 'score_a', 'score_b', 'players', 'completed'
        )


class UpdateEventPlayerSerializer(ModelSerializer):
    assistant_id = IntegerField(
        source="id", label='assistant_id', write_only=True
    )

    class Meta:
        model = EventPlayer
        fields = ['id', 'assistant_id']

    def update(self, instance, validated_data):
        if instance.event.completed != Event.EventState.PENDING:
            raise ValidationError('Event must be in pending state')
        instance.goals_in_game += 1
        if 'id' in validated_data:
            assistant_player = EventPlayer.objects.get(
                                    id=validated_data.pop('id'))
            assistant_player.assists_in_game += 1
            assistant_player.save()
        instance.save()
        return instance
