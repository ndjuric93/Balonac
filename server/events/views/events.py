from rest_framework import permissions, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from events.models import Event
from events.serializers import (
    EventSerializer,
    SingleEventSerializer,
    CreateEventSerializer,
    UpdateEventSerializer
)


class EventsViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    GenericViewSet):
    queryset = Event.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_serializer_class(self):
        if self.action == 'list':
            return EventSerializer
        elif self.action == 'retrieve':
            return SingleEventSerializer
        elif self.action == 'create':
            return CreateEventSerializer
        else:
            return UpdateEventSerializer
