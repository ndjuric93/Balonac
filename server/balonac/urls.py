"""balonac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from players.views import CreatePlayerView, PlayersViewSet
from events.views.create import CreatedEventViewSet
from events.views import RetrieveEventsViewSet

router = DefaultRouter()
# router.register(r'event', EventViewSet)
router.register(r'event/create', CreatedEventViewSet)
router.register(r'event', RetrieveEventsViewSet)
router.register(r'player', PlayersViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
    path('api/v1/player/create', CreatePlayerView.as_view()),
    path('api/v1/', include(router.urls)),
    path('api/admin/', admin.site.urls),
]
