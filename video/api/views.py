from django.db.models import Q
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from video.models import Playlist, Video, Channel
from .serializers import PlaylistSerializer, VideoSerializer, ChannelSerializers
from .pagination import CustomPagination

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializers
    pagination_class = PageNumberPagination
    lookup_field = "channel_id"
    
    
class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    pagination_class = PageNumberPagination
    lookup_field = "playlist_id"


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('-published_at')
    serializer_class = VideoSerializer
    pagination_class = PageNumberPagination
    lookup_field = "video_id"
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title',)
    pagination_class = CustomPagination