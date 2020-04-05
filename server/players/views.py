from rest_framework import permissions, mixins, generics
from rest_framework.viewsets import GenericViewSet

from players.models import Player
from players.serializers import PlayerSerializer, CreatePlayerSerializer


class PlayersViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class CreatePlayerView(generics.CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = CreatePlayerSerializer
    # permission_classes = [permissions.IsAdminUser]
