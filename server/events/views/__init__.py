from rest_framework import permissions, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from events.models import Event
from events.serializers import EventSerializer, SingleEventSerializer


class RetrieveEventsViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            GenericViewSet):
    queryset = Event.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = EventSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return EventSerializer
        elif self.action == 'retrieve':
            return SingleEventSerializer
