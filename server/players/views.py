from rest_framework import permissions, mixins, generics
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from players.models import Player
from players.serializers import PlayerSerializer, CreatePlayerSerializer


class PlayersViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class CreatePlayerView(generics.CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = CreatePlayerSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
