import requests
from .models import Playlist, Video, Channel
from django.conf import settings
from django.core.cache import cache
from googleapiclient.discovery import build
import google.generativeai as genai
from django.utils.dateparse import parse_duration
import isodate

YOUTUBE_API_KEY = settings.API_KEY
API_KEY = settings

CHANNEL_IDS = [settings.CHANNEL_ID]

def fetch_channels():
    channels = cache.get('channels')

    if not channels:
        channels = []
        for channel_id in CHANNEL_IDS:
            url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={YOUTUBE_API_KEY}"
            response = requests.get(url).json()

            for item in response.get("items", []):
                channel_name = item["snippet"]["title"]
                thumbnail = (
                    item["snippet"]["thumbnails"].get("high") or 
                    item["snippet"]["thumbnails"].get("medium") or 
                    item["snippet"]["thumbnails"].get("default") or 
                    {}
                ).get("url", "")

                if not Channel.objects.filter(channel_id=channel_id).exists():
                    Channel.objects.create(
                        channel_id=channel_id,
                        channel_name=channel_name,
                        thumbnail=thumbnail
                    )

                channels.append({
                    "channel_id": channel_id,
                    "channel_name": channel_name,
                    "thumbnail": thumbnail
                })

        cache.set('channels', channels, timeout=3600)

def fetch_youtube_data():
    playlists = cache.get('playlists')

    if not playlists:
        playlists = []
        for channel_id in CHANNEL_IDS:
            next_page_token = ""
            
            while next_page_token is not None:
                url = f"https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId={channel_id}&maxResults=50&pageToken={next_page_token}&key={YOUTUBE_API_KEY}"
                response = requests.get(url).json()

                try:
                    channel_obj = Channel.objects.get(channel_id=channel_id)
                except Channel.DoesNotExist:
                    continue

                for item in response.get("items", []):
                    playlist_id = item["id"]
                    title = item["snippet"]["title"]
                    thumbnail = (
                        item["snippet"]["thumbnails"].get("high") or 
                        item["snippet"]["thumbnails"].get("medium") or 
                        item["snippet"]["thumbnails"].get("default") or 
                        {}
                    ).get("url", "")

                    if "short" not in title.lower():
                        if not Playlist.objects.filter(playlist_id=playlist_id).exists():
                            Playlist.objects.create(
                                playlist_id=playlist_id,
                                playlist_name=title,
                                thumbnail=thumbnail,
                                channel=channel_obj,
                                is_active=True
                            )

                        playlists.append({
                            "playlist_id": playlist_id,
                            "playlist_name": title,
                            "thumbnail": thumbnail,
                            "channel_name": channel_obj.channel_name,
                            "channel_id": channel_obj.channel_id
                        })

                next_page_token = response.get("nextPageToken")

        cache.set('playlists', playlists, timeout=3600)

    fetch_videos(playlists)



def fetch_videos(playlists):
    for playlist in playlists:
        playlist_id = playlist['playlist_id']
        playlist_obj = Playlist.objects.get(playlist_id=playlist_id)
        next_page_token = ""

        while next_page_token is not None:
            url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={playlist_id}&pageToken={next_page_token}&key={YOUTUBE_API_KEY}"
            response = requests.get(url).json()

            video_ids = []
            video_data = {}

            for item in response.get("items", []):
                video_id = item["snippet"]["resourceId"]["videoId"]
                video_ids.append(video_id)

                video_data[video_id] = {
                    "title": item["snippet"]["title"],
                    "description": item["snippet"].get("description", ""),
                    "thumbnail": (
                        item["snippet"]["thumbnails"].get("high") or 
                        item["snippet"]["thumbnails"].get("medium") or 
                        item["snippet"]["thumbnails"].get("default") or 
                        {}
                    ).get("url", ""),
                    "video_url": f"https://www.youtube.com/watch?v={video_id}",
                    "published_at": item["snippet"]["publishedAt"],
                }

            video_durations = {}
            video_views = {}
            video_likes = {}
            video_dislikes = {}
            if video_ids:
                video_ids_str = ",".join(video_ids)
                
                video_details_url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails,statistics&id={video_ids_str}&key={YOUTUBE_API_KEY}"
                video_details_response = requests.get(video_details_url).json()

                for item in video_details_response.get("items", []):
                    video_id = item["id"]
                    
                    duration_iso = item["contentDetails"]["duration"]
                    duration = isodate.parse_duration(duration_iso)
                    video_durations[video_id] = duration

                    video_views[video_id] = item["statistics"].get("viewCount", "0")
                    video_likes[video_id] = item["statistics"].get("likeCount", "0")
                    video_dislikes[video_id] = item["statistics"].get("dislikeCount", "0")

            for video_id in video_ids:
                if not Video.objects.filter(video_id=video_id).exists():
                    Video.objects.create(
                        video_id=video_id,
                        playlist=playlist_obj,
                        title=video_data[video_id]["title"],
                        description=video_data[video_id]["description"],
                        thumbnail=video_data[video_id]["thumbnail"],
                        url=video_data[video_id]["video_url"],
                        duration=video_durations.get(video_id, None),
                        view_count=video_views.get(video_id, 0),
                        like_count=video_likes.get(video_id, 0),
                        dislike_count=video_dislikes.get(video_id, 0),
                        published_at=video_data[video_id]["published_at"],
                        is_active=True
                    )

            next_page_token = response.get("nextPageToken")
            
            
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)