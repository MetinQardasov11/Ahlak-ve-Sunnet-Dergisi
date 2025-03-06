from django.urls import path
from .views import playlists, videos, video_detail, video_not_found

app_name = 'video'

urlpatterns = [
    path('', playlists, name='playlists'),
    path('<str:playlist_id>/', videos, name='videos'),
    path('<str:playlist_id>/<str:video_id>', video_detail, name='video_detail'),
    # path('not-found/', video_not_found, name='video_not_found'),
]