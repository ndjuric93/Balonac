from django.http import HttpResponse
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from events.models import Event
from events.serializers import EventSerializer
from players.models import Player
from players.serializers import PlayerSerializer


class EventViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventForPlayersViewSet(mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        event = self.get_object()
        player = Player.objects.get(id=request.data['player']['id'])
        event.players.add(player)
        return HttpResponse(EventSerializer(event).data)

    def partial_update(self, request, *args, **kwargs):
        scorer = Player.objects.get(id=request.data['player']['goal'])
        scorer.goals += 1
        scorer.save()
        if 'assist' in request.data['player']:
            assister = Player.objects.get(id=request.data['player']['assist'])
            assister.assists += 1
            assister.save()
        return HttpResponse(status=HTTP_200_OK)
