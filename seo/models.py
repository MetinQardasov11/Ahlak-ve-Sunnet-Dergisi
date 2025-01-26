from django.db import models
from base.models import TemplatePage

class MetaTags(models.Model):
    KEYWORDS = 'keywords'
    DESCRIPTION = 'description'
    TITLE = 'title'
    AUTHOR = 'author'
    VIEWPORT = 'viewport'

    TAG_CHOICES = [
        (KEYWORDS, 'Anahtar Kelimeler (keywords)'),
        (DESCRIPTION, 'Açıklama (description)'),
        (TITLE, 'Başlık (title)'),
        (AUTHOR, 'Yazar (author)'),
        (VIEWPORT, 'Görünüm Ayarları (viewport)'),
    ]

    page = models.ForeignKey(TemplatePage, on_delete=models.CASCADE, related_name="meta_tags", verbose_name="Meta etiketinin bağlı olduğu sayfa.")
    tag_type = models.CharField(max_length=30, choices=TAG_CHOICES, verbose_name="Meta etiketinin türü (örn: keywords, description).")
    content = models.TextField(verbose_name="Meta etiketinin içeriği (örn: anahtar kelimeler veya açıklama).")
    is_active = models.BooleanField(default=True, verbose_name="Bu meta etiketinin aktif olup olmadığını belirler.")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Meta etiketinin son güncellenme zamanı.")

    def __str__(self):
        return f"{self.get_tag_type_display()} - {self.content[:50]}"

    class Meta:
        verbose_name = "Meta Etiketi"
        verbose_name_plural = "Meta Etiketleri"
        ordering = ['-updated_at']
        

class SocialTag(models.Model):
    OG_TITLE = 'og:title'
    OG_DESCRIPTION = 'og:description'
    OG_IMAGE = 'og:image'
    TWITTER_TITLE = 'twitter:title'
    TWITTER_DESCRIPTION = 'twitter:description'
    TWITTER_IMAGE = 'twitter:image'

    TAG_CHOICES = [
        (OG_TITLE, 'Open Graph Başlık (og:title)'),
        (OG_DESCRIPTION, 'Open Graph Açıklama (og:description)'),
        (OG_IMAGE, 'Open Graph Görsel (og:image)'),
        (TWITTER_TITLE, 'Twitter Başlık (twitter:title)'),
        (TWITTER_DESCRIPTION, 'Twitter Açıklama (twitter:description)'),
        (TWITTER_IMAGE, 'Twitter Görsel (twitter:image)'),
    ]

    template_page = models.ForeignKey(TemplatePage, on_delete=models.CASCADE, related_name='social_tags', verbose_name="Bu sosyal medya etiketinin bağlı olduğu sayfa.", null=True,  blank=True)
    tag_type = models.CharField(max_length=30, choices=TAG_CHOICES, verbose_name="Etiket türünü seçin (örneğin, 'og:title', 'twitter:image').")
    content = models.TextField(verbose_name="Etiket içeriği (örneğin, başlık, açıklama veya görsel URL'si).")
    is_active = models.BooleanField(default=True, verbose_name="Bu etiketin aktif olup olmadığını belirler.")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Etiketin son güncellenme tarihi ve saati.")

    def __str__(self):
        return f"{self.get_tag_type_display()} - {self.content[:50]}"

    class Meta:
        verbose_name = "Sosyal Medya Etiketi"
        verbose_name_plural = "Sosyal Medya Etiketleri"
        ordering = ['-updated_at']