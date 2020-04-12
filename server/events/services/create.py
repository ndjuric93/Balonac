from events.models import Event, EventPlayer
from players.models import Player


def create_event(event_data, event_players):
    """
    Create event with given data.

    Event is created, and a set of passed players is registered to it.
    """
    print(event_data)
    event = Event.objects.create(**event_data)
    return event


def update_event(event, data):
    """
    Register given players to a given event.
    """
    if 'location' in data:
        event.location = data['location']
    if 'date' in data:
        event.location = data['date']
    event.save()
    for player in players:
        EventPlayer(
            event=event,
            player=Player.objects.get(id=player)
        ).save()
    return event
