from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse

class TemplatePage(models.Model):
    PAGE_CHOICES = [
        ('base/index.html', 'Ana Sayfa'),
        ('base/about.html', 'Hakkımızda'),
        ('base/galery.html', 'Galeri'),
        ('service/services.html', 'Hizmetler'),
        ('service/service-details.html', 'Hizmet Detayları'),
        ('blog/blogs.html', 'Blog'),
        ('blog/blog-details.html', 'Blog Detayları'),
        ('contact/contact.html', 'İletişim'),
        ('base/404.html', '404 Sayfası'),
    ]

    url = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name="Sayfanın URL yolu")
    template_name = models.CharField(max_length=50, choices=PAGE_CHOICES, verbose_name="Sayfa türü")
    title = models.CharField(max_length=255, verbose_name="Sayfanın başlığı")
    description = models.TextField(blank=True, null=True, verbose_name="Sayfanın açıklaması")
    is_active = models.BooleanField(default=True, verbose_name="Sayfanın aktif olup olmadığını belirler")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Sayfanın oluşturulma tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Sayfanın güncellenme tarihi")

    def get_absolute_url(self):
        return f"/{self.url}/"

    def __str__(self):
        return f"{self.template_name} ({self.url})"

    class Meta:
        verbose_name = "Sayfa"
        verbose_name_plural = "Sayfalar"


class GeneralItem(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Genel Bilgi Başlığı")
    description = RichTextField(verbose_name = "Açıklama")
    nav_img = models.ImageField(upload_to='nav_img', verbose_name = "Navigasyon Resmi")
    footer_img = models.ImageField(upload_to='footer_img', verbose_name = "Footer Resmi")
    favicon_img = models.ImageField(upload_to='favicon_img', verbose_name = "Favicon Resmi", null=True, blank=True)
    facebook = models.URLField(verbose_name = "Facebook Linki", null=True, blank=True)
    twitter = models.URLField(verbose_name = "Twitter Linki", max_length=600, null=True, blank=True)
    instagram = models.URLField(verbose_name = "İnstagram Linki", max_length=600, null=True, blank=True)
    youtube = models.URLField(verbose_name = "Youtube Linki", max_length=600, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Genel Bilgiler"        
        

class HomeSlider(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Slider Başlığı")
    description = RichTextField(verbose_name = "Açıklama", blank=True, null=True)
    image = models.ImageField(upload_to='slider_img', verbose_name = "Slider Resmi")
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Ana Sayfa Sliderları"
        
        
class About(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Başlık")
    description = RichTextField(verbose_name = "Açıklama")
    image = models.ImageField(upload_to='about_img', verbose_name = "Resim")
    video = models.FileField(upload_to='about_video', verbose_name = "Video")
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Hakkımızda"
        
        
class IslamCondition(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Şart Başlığı")
    image = models.ImageField(upload_to='condition_img',verbose_name='Resim')
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "İslamın Şartları"
        
        
class StatisticInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Bilgi Başlığı")
    description = RichTextField(verbose_name = "Açıklama")   
    image = models.ImageField(upload_to='statistic_img', verbose_name='Resim')
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "İstatistik için genel bilgiler"
        
        
class Statistic(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Statistik Bilgi Başlığı")
    value = models.IntegerField(verbose_name='Statistik Değer')
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "İstatistik Bilgileri"
        
        
class Subscribe(models.Model):
    email = models.EmailField(verbose_name = "Email")
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Aboneler"
        
        
class Galery(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Galeri Başlığı")
    image = models.ImageField(upload_to='galery_img', verbose_name='Resim')
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Galeri"
        
        
class PageBunner(models.Model):
    
    title = models.CharField(max_length=200, verbose_name = "Banner için başlık")
    
    about_title = models.CharField(max_length=200, verbose_name = "Hakkımızda banner Başlığı")
    about_img = models.ImageField(verbose_name = "Hakkımızda banner resim", upload_to='banner')
    
    service_title = models.CharField(max_length=200, verbose_name = "Hizmetler banner Başlığı")
    service_img = models.ImageField(verbose_name = "Hizmetler banner resim", upload_to='banner')
    
    service_detail_title = models.CharField(max_length=200, verbose_name = "Hizmet Detayları banner Başlığı", blank=True, null=True)
    service_detail_img = models.ImageField(verbose_name = "Hizmet Detayları banner resim", upload_to='banner')
    
    blog_title = models.CharField(max_length=200, verbose_name = "Bloglar banner Başlığı")
    blog_img = models.ImageField(verbose_name = "Bloglar banner resim", upload_to='banner')
    
    blog_detail_title = models.CharField(max_length=200, verbose_name = "Blog Detayları banner Başlığı", blank=True, null=True)
    blog_detail_img = models.ImageField(verbose_name = "Blog Detayları banner resim", upload_to='banner')
    
    galery_title = models.CharField(max_length=200, verbose_name = "Galeri banner Başlığı")
    galery_img = models.ImageField(verbose_name = "Galeri banner resim", upload_to='banner')
    
    contact_title = models.CharField(max_length=200, verbose_name = "İletişim banner Başlığı")
    contact_img = models.ImageField(verbose_name = "İletişim banner resim", upload_to='banner')
    
    error_title = models.CharField(max_length=200, verbose_name = "Error banner Başlığı", blank=True, null=True)
    error_img = models.ImageField(verbose_name = "Error banner resim", blank=True, null=True, upload_to='banner')
    
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sayfa Bannerları"