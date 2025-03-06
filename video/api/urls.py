from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaylistViewSet, VideoViewSet, ChannelViewSet

router = DefaultRouter()
router.register(r'channels', ChannelViewSet)
router.register(r'playlists', PlaylistViewSet)
router.register(r'videos', VideoViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]