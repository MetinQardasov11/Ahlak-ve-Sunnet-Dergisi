from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from django.contrib import messages
from django.shortcuts import redirect
from .models import Channel, Playlist, Video, Language
from .utils import fetch_channels, fetch_youtube_data

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('channel_name', 'count_playlists')
    search_fields = ('channel_name', 'channel_id')
    
admin.site.register(Language)

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('playlist_id', 'playlist_name', 'count_videos', 'get_languages', 'is_active')
    search_fields = ('playlist_name', 'playlist_id')
    
    def get_languages(self, obj):
        return ", ".join([language.code for language in obj.languages.all()])
    get_languages.short_description = 'Languages'


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_id', 'playlist', 'is_active', 'published_at')
    search_fields = ('video_id', 'title', 'view_count')
    ordering = ('-published_at', )
    list_per_page = 50
     
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['fetch_button'] = True
        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("fetch-youtube/", self.fetch_youtube, name="fetch_youtube"),
        ]
        return custom_urls + urls

    def fetch_youtube(self, request):
        fetch_channels()
        fetch_youtube_data()
        self.message_user(request, "YouTube kanalları və videolar güncellendi!", messages.SUCCESS)
        return redirect(request.META.get("HTTP_REFERER", "/admin/"))