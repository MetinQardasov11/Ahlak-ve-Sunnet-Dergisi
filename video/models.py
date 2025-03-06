from django.db import models

LANGUAGES = [ 
        ('tr', 'Turkish'),
        ('ar', 'Arabic'),
        ('kk', 'Kurdish'),
    ]

class Language(models.Model):
    code = models.CharField(choices=LANGUAGES, max_length=2)
    
    def __str__(self):
        return f'{self.code}'
    
    class Meta:
        verbose_name_plural = "Diller"

class Channel(models.Model):
    channel_id = models.CharField(max_length=255, unique=True, help_text="Kanal ID'si")
    channel_name = models.CharField(max_length=255, help_text="Kanal Adı")
    thumbnail = models.URLField(help_text="Kanal Resmi")
    
    def __str__(self):
        return f'{self.channel_name}'
    
    def count_playlists(self):
        return self.playlists.count()

    class Meta:
        verbose_name_plural = "Kanallar"
    
class Playlist(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="playlists", help_text="Kanal")
    playlist_id = models.CharField(max_length=255, unique=True, help_text="Playlist ID'si")
    playlist_name = models.CharField(max_length=255, help_text="Playlist Adı")
    thumbnail = models.URLField(help_text="Playlist Resmi")
    is_active = models.BooleanField(default=True, help_text="Aktif Mi?", blank=True, null=True)
    languages = models.ManyToManyField(Language, blank=True, help_text="Seçilmiş dillər", related_name="playlists")

    def __str__(self):
        return f'{self.playlist_name}'
    
    def count_videos(self):
        return self.videos.count()
    
    def get_languages(self):
        return self.languages.split(',') if self.languages else []

    class Meta:
        verbose_name_plural = "Oynatma Listeleri"


class Video(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name="videos", null=True, blank=True, help_text="Playlist")
    video_id = models.CharField(max_length=255, unique=True, help_text="Video ID'si")
    title = models.CharField(max_length=255, help_text="Video Başlığı")
    description = models.TextField(blank=True, null=True, help_text="Video Açıklaması")
    thumbnail = models.URLField(help_text="Video Resmi")
    url = models.URLField(help_text="Video URL'si")
    duration = models.DurationField(blank=True, null=True, help_text="Video Süresi")
    view_count = models.IntegerField(null=True, blank=True, help_text="Görüntülenme Sayısı")
    like_count = models.IntegerField(help_text="Beğeni Sayısı", default=0, null=True, blank=True)
    dislike_count = models.IntegerField(help_text="Beğenmeme Sayısı", default=0, null=True, blank=True)
    languages = models.ManyToManyField(Language, blank=True, help_text="Seçilmiş dillər", related_name="videos")
    is_active = models.BooleanField(default=True, help_text="Aktif Mi?")
    published_at = models.DateTimeField(help_text="Yayınlanma Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Videolar"