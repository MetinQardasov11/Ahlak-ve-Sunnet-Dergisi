from django.db import models
from django.utils.text import slugify
from django.utils.translation import get_language
from django.conf import settings
from ckeditor.fields import RichTextField
from base.models import Language

LANGUAGES = [
        ('tr', 'Türkçe'),
        ('ar', 'Arapça'),
        ('kk', 'Kürtçe'),
    ]


class BlogCategory(models.Model):
    
    language = models.CharField(max_length=2, choices=LANGUAGES, default='tr', verbose_name='Dil', blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Kategori Adı', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name='Slug')
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def get_translated_name(self):
        lang = get_language()
        return getattr(self, f'name_{lang}', None) or ''

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = 'Makale Kategorileri'
        

class Blog(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name='Kategori')
    language = models.CharField(max_length=2, choices=LANGUAGES, default='tr', verbose_name='Dil', blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name='Makale Başlığı', null=True, blank=True)
    description = RichTextField(verbose_name='Açıklama', null=True, blank=True)
    image = models.ImageField(verbose_name='Makale Resmi', upload_to='blog_img', null=True, blank=True)
    author = models.CharField(max_length=100, verbose_name='Makale Yazarı', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name='Slug')

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
        
    def __str__(self):
        return str(self.title)
    
    def get_translated_blog(self):
        lang = get_language()
        return getattr(self, f'title_{lang}', None), getattr(self, f'description_{lang}', None) or ''
    
    class Meta:
        verbose_name_plural = 'Makaleler'
        
        
class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images', verbose_name = "Blog")
    image = models.ImageField(upload_to='blog_img', verbose_name = "Resim", null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return f"{self.blog.title} - Image {self.id}"
    
    class Meta:
        verbose_name_plural = "Makale Alt Resimleri"