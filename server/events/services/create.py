from events.models import Event, EventPlayer
from players.models import Player


def create_event(event_data, event_players):
    """
    Create event with given data.

    Event is created, and a set of passed players is registered to it.
    """
    event = Event.objects.create(**event_data)
    for player in event_players:
        EventPlayer.objects.create(event=event, player=player['player'])
    return event


def update_event(event, event_data, event_players):
    """
    Register given players to a given event.
    """
    if 'location' in event_data:
        event.location = event_data['location']
    if 'date' in event_data:
        event.date = event_data['date']
    event.save()
    for player in event_players:
        EventPlayer.objects.get_or_create(event=event, player=player['player'])
    return event
