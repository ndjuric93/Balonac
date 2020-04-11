from django.http import HttpResponse
from rest_framework import permissions, mixins
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from events.models import Event, EventPlayer
from events.serializers import EventSerializer, SingleEventSerializer
from players.models import Player
from players.serializers import PlayerSerializer


class EventViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    queryset = Event.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def update(self, request, *args, **kwargs):
        event = self.get_object()
        for event_player in event.players.all():
            event_player.player.appearances += 1
            event_player.player.goals += event_player.goals
            event_player.player.assists += event_player.assists
        event_player.player.save()
        event.completed = True
        event.save()
        return HttpResponse(status=HTTP_200_OK)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SingleEventSerializer
        return EventSerializer


class EventForPlayersViewSet(mixins.UpdateModelMixin,
                             mixins.CreateModelMixin,
                             mixins.DestroyModelMixin,
                             GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def update(self, request, *args, **kwargs):
        event = self.get_object()
        if event.completed:
            return HttpResponse(status=HTTP_403_FORBIDDEN)
        player = Player.objects.get(id=request.data['player']['id'])
        event_player = EventPlayer(player=player, name=player.name)
        event_player.save()
        event.players.add(event_player)
        return HttpResponse(EventSerializer(event).data)

    def partial_update(self, request, *args, **kwargs):
        if self.get_object().completed:
            return HttpResponse(status=HTTP_403_FORBIDDEN)
        player_data = request.data['player']
        scorer = EventPlayer.objects.get(id=player_data['goal'])
        scorer.goals += 1
        scorer.save()
        if 'assist' in request.data['player']:
            assister = EventPlayer.objects.get(id=player_data['assist'])
            assister.assists += 1
            assister.save()
        return HttpResponse(status=HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        player = Player.objects.get(id=request.data['player']['id'])
        player.delete()
        player.save()
        return HttpResponse(status=HTTP_200_OK)
