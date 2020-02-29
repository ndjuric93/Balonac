from rest_framework import permissions, generics

from players.models import Player
from players.serializers import PlayerSerializer, CreatePlayerSerializer


class ListPlayersView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class CreatePlayerView(generics.CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = CreatePlayerSerializer
    permission_classes = [permissions.IsAdminUser]
