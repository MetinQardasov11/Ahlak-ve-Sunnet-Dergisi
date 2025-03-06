from rest_framework import serializers
from video.models import Playlist, Video, Channel
from datetime import timedelta
from django.utils.text import slugify


class ChannelSerializers(serializers.ModelSerializer):
    playlists_count = serializers.IntegerField(source='count_playlists', read_only=True)
    slug = serializers.SerializerMethodField()
    
    class Meta:
        model = Channel
        fields = ['id', 'channel_id', 'channel_name', 'thumbnail', 'playlists_count', 'slug']
        
    def get_slug(self, obj):
        clean_channel_name = obj.channel_name.split("|")[0].strip()
        return slugify(clean_channel_name)


class PlaylistSerializer(serializers.ModelSerializer):
    video_count = serializers.IntegerField(source='count_videos', read_only=True)
    channel_info = serializers.SerializerMethodField()
    channel = serializers.PrimaryKeyRelatedField(queryset=Channel.objects.all(), write_only=True)
    slug = serializers.SerializerMethodField()


    class Meta:
        model = Playlist
        fields = ['id', 'playlist_id', 'playlist_name', 'channel', 'channel_info', 'thumbnail', 'video_count', 'slug']


    def get_channel_info(self, obj):
        return {
            "channel_id": obj.channel.channel_id,
            "channel_name": obj.channel.channel_name,
        }
        
    def get_slug(self, obj):
        clean_playlist_name = obj.playlist_name.split("|")[0].strip()
        return slugify(clean_playlist_name)


class VideoSerializer(serializers.ModelSerializer):
    playlist_info = serializers.SerializerMethodField()
    channel_info = serializers.SerializerMethodField()
    playlist = serializers.PrimaryKeyRelatedField(queryset=Playlist.objects.all(), write_only=True)
    # channel = serializers.PrimaryKeyRelatedField(queryset=Channel.objects.all(), write_only=True)
    published_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    duration = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ['id', 'video_id', 'title', 'playlist', 'playlist_info', 'channel_info', 'duration', 'view_count', 'description', 'thumbnail', 'url', 'slug', 'published_at']
        

    def get_playlist_info(self, obj):
        return {
            "playlist_id": obj.playlist.playlist_id,
            "playlist_name": obj.playlist.playlist_name,
        }
        
        
    def get_channel_info(self, obj):
        return {
            "channel_id": obj.playlist.channel.channel_id,
            "channel_name": obj.playlist.channel.channel_name,
            "thumbnail" : obj.playlist.channel.thumbnail
        }
        
    def get_slug(self, obj):
        clean_video_title = obj.title.split("|")[0].strip()
        return slugify(clean_video_title)
        

    def get_duration(self, obj):
        if not obj.duration:
            return None
        
        if isinstance(obj.duration, str):
            return obj.duration
        
        if isinstance(obj.duration, timedelta):
            total_seconds = int(obj.duration.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            if hours > 0:
                return f"{hours}:{minutes:02}:{seconds:02}"
            return f"{minutes}:{seconds:02}"

        return str(obj.duration)