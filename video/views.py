from django.shortcuts import render, get_object_or_404, redirect
from .models import Playlist, Video, Language
from django.core.paginator import Paginator
from django.utils.translation import get_language


def playlists(request):
    current_language = get_language()
    selected_language_code = request.GET.get('language', current_language)
    
    playlists = Playlist.objects.filter(is_active=True)

    if selected_language_code:
        language = Language.objects.filter(code=selected_language_code).first()
        if language:
            playlists = playlists.filter(languages=language)

    paginator = Paginator(playlists, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'playlists': playlists,
        'page_obj': page_obj,
        'selected_language': selected_language_code,
    }
    
    return render(request, 'video/playlist.html', context)



def videos(request, playlist_id):
    playlist = get_object_or_404(Playlist, playlist_id=playlist_id)
    current_language = get_language()
    selected_language_code = request.GET.get('language', current_language)
    videos = Video.objects.filter(playlist=playlist)
    
    if selected_language_code:
        language = Language.objects.filter(code=selected_language_code).first()
        if language:
            videos = videos.filter(languages=language)
    
    paginator = Paginator(videos, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'playlist': playlist,
        'videos': videos,
        'page_obj': page_obj,
        'selected_language': selected_language_code
    }
    
    return render(request, 'video/videos.html', context)



def video_detail(request, playlist_id, video_id):
    user_language = get_language()
    try:
        playlist = Playlist.objects.get(playlist_id=playlist_id)
        video = Video.objects.get(video_id=video_id, playlist=playlist)

        # if user_language not in [language.code for language in video.languages.all()]:
        #     return redirect('base:video_not_found')

    except Video.DoesNotExist:
        return redirect('base:video_not_found')
    
    random_videos = Video.objects.filter(is_active=True).exclude(title='Private video').order_by('?')[:10]

    context = {
        'playlist': playlist,
        'video': video,
        'random_videos': random_videos
    }
    return render(request, 'video/video-details.html', context)
