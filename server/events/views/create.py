from django.http import HttpResponse
from rest_framework import permissions, mixins
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from events.models import Event, EventPlayer
from events.serializers import (
    EventSerializer,
    SingleEventSerializer,
    CreateEventSerializer
)
from events.services.create import create_event
from players.models import Player
from players.serializers import PlayerSerializer


class CreatedEventViewSet(mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          GenericViewSet):
    queryset = Event.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = CreateEventSerializer
