from rest_framework import permissions, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from events.models import Event
from events.serializers import (
    EventSerializer, SingleEventSerializer, CreateEventSerializer
)
