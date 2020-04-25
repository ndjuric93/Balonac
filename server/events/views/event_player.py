from rest_framework import permissions, mixins
from rest_framework.viewsets import GenericViewSet

from rest_framework_simplejwt.authentication import JWTAuthentication

from events.serializers import UpdateEventPlayerSerializer
from events.models import EventPlayer


class UpdateEventPlayer(mixins.UpdateModelMixin,
                        GenericViewSet):
    queryset = EventPlayer.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = UpdateEventPlayerSerializer
