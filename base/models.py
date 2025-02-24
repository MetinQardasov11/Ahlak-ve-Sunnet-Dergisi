from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse

class DateModel(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")


class GeneralItem(DateModel):
    title = models.CharField(max_length=200, verbose_name = "Site Ismi", null=True, blank=True)
    description = RichTextField(verbose_name = "Açıklama", blank=True, null=True)
    nav_img = models.ImageField(upload_to='nav_img', verbose_name = "Navigasyon Resmi", null=True, blank=True)
    footer_img = models.ImageField(upload_to='footer_img', verbose_name = "Footer Resmi", null=True, blank=True)
    favicon_img = models.ImageField(upload_to='favicon_img', verbose_name = "Favicon Resmi", null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Genel Bilgiler"     
        
        
class NavbarItem(DateModel):
    
    POSITION_CHOICES = [
        ('both', 'Her ikisi'),
        ('navbar', 'Navbar'),
        ('footer', 'Footer'),
    ]
    
    title = models.CharField(max_length=100, verbose_name="Başlık", blank=True, null=True)
    url = models.CharField(max_length=200, verbose_name="URL", blank=True, null=True)
    order = models.IntegerField(default=0, verbose_name="Sıra")
    is_active = models.BooleanField(default=True, verbose_name="Aktif mi?")
    position = models.CharField(max_length=30, choices=POSITION_CHOICES, default='both', verbose_name="Menyu yeri", null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.title.strip().lower().replace(" ", "") == "anasayfa":
            self.url = "/"
        else: 
            if not self.url or self.url != slugify(self.title):
                self.url = f"/{slugify(self.title)}/"
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return f'/{self.url}'

        
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Navigasyon Menüsü"

class HomeSlider(DateModel):
    title = models.CharField(max_length=200, verbose_name = "Slider Başlığı", blank=True, null=True)
    description = RichTextField(verbose_name = "Açıklama", blank=True, null=True)
    image = models.ImageField(upload_to='slider_img', verbose_name = "Slider Resmi", blank=True, null=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Ana Sayfa Sliderları"
        
        
class About(DateModel):
    title = models.CharField(max_length=200, verbose_name = "Başlık", blank=True, null=True)
    description = RichTextField(verbose_name = "Açıklama", blank=True, null=True)
    image = models.ImageField(upload_to='about_img', verbose_name = "Resim", blank=True, null=True)
    video = models.FileField(upload_to='about_video', verbose_name = "Video", blank=True, null=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Hakkımızda"
        
        
class IslamCondition(DateModel):
    title = models.CharField(max_length=200, verbose_name = "Şart Başlığı")
    image = models.ImageField(upload_to='condition_img',verbose_name='Resim')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "İslamın Şartları"
        
        
class StatisticInfo(DateModel):
    title = models.CharField(max_length=200, verbose_name = "Bilgi Başlığı", blank=True, null=True)
    description = RichTextField(verbose_name = "Açıklama", blank=True, null=True)   
    image = models.ImageField(upload_to='statistic_img', verbose_name='Resim', blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "İstatistik için genel bilgiler"
        
        
class Statistic(DateModel):
    title = models.CharField(max_length=200, verbose_name = "Statistik Bilgi Başlığı", blank=True, null=True)
    value = models.IntegerField(verbose_name='Statistik Değer', blank=True, null=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "İstatistik Bilgileri"
        
        
class Subscribe(DateModel):
    email = models.EmailField(verbose_name = "Email")
    
    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Aboneler"
        
        
class Galery(DateModel):
    title = models.CharField(max_length=200, verbose_name = "Galeri Başlığı", blank=True, null=True)
    image = models.ImageField(upload_to='galery_img', verbose_name='Resim')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Galeri"
        
        
class PageBanner(DateModel):
    
    PAGE_CHOICES = [
        ('home', 'Ana Sayfa'),
        ('about', 'Hakkımızda'),
        ('service', 'Hizmetler'),
        ('service_detail', 'Hizmet Detayları'),
        ('blog', 'Bloglar'),
        ('blog_detail', 'Blog Detayları'),
        ('galery', 'Galeri'),
        ('contact', 'İletişim'),
        ('error', 'Error'),
    ]
    
    page = models.CharField(max_length=20, choices=PAGE_CHOICES, unique=True, verbose_name="Sayfa", blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name="Banner Başlığı", blank=True, null=True)
    image = models.ImageField(verbose_name="Banner Resmi", upload_to='banner', blank=True, null=True)
    
    

    def __str__(self):
        return self.page

    class Meta:
        verbose_name_plural = "Sayfa Bannerları"
        
        
class MetaTag(DateModel):
    META_NAME_CHOICES = [
        ("author", "Yazar"),
        ("description", "Açıklama"),
        ("keywords", "Anahtar Kelimeler"),
        ("robots", "Robots"),
        ("viewport", "Viewport"),
        ("og:title", "Open Graph Başlığı"),
        ("og:description", "Open Graph Açıklaması"),
        ("og:image", "Open Graph Görseli"),
        ("twitter:title", "Twitter Başlığı"),
        ("twitter:description", "Twitter Açıklaması"),
        ("twitter:image", "Twitter Görseli"),
    ]
    
    page_name = models.ForeignKey(NavbarItem, on_delete=models.CASCADE, blank=True, null=True, related_name="meta_tags")
    name = models.CharField(max_length=50, choices=META_NAME_CHOICES, help_text="Meta adı veya özelliği", blank=True, null=True)
    content = models.TextField(help_text="Meta tag içeriği (content)", blank=True, null=True)
    slug = models.SlugField(blank=True, null=True, help_text='Otomatik oluşturulur. Boş bırakınız.')
    
    def save(self, *args, **kwargs):
        if self.page_name:
            page_title = self.page_name.title.strip().lower().replace(" ", "")
            
            if page_title == "anasayfa":
                self.slug = ""
            else:
                self.slug = slugify(page_title)
        else:
            self.slug = ""
        super().save(*args, **kwargs)

    
    def __str__(self):
        return f"{self.page_name} - {self.name}"
    
    class Meta:
        verbose_name_plural = "SEO"
        
        
class DynamicPage(DateModel):
    
    POSITION_CHOICES = [
        ('both', 'Her ikisi'),
        ('navbar', 'Navbar'),
        ('footer', 'Footer'),
    ]
    
    title = models.CharField(max_length=200, verbose_name = "Sayfa Adı")
    banner_img = models.ImageField(upload_to='dynamic_page_banner', verbose_name = "Banner", blank=True, null=True)
    content = RichTextField(verbose_name = "İçerik")
    slug = models.SlugField(unique=True, verbose_name = "URL", blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return f"/{self.slug}/"
        
    class Meta:
        verbose_name_plural = "Dinamik Sayfalar"


class SocialMedia(DateModel):
    name = models.CharField(max_length=200, verbose_name = "Sosyal Medya Başlığı", blank=True, null=True)
    url = models.CharField(max_length=200, verbose_name = "URL", blank=True, null=True)
    icon = models.CharField(max_length=200, verbose_name = "Icon", blank=True, null=True, help_text="Font Awesome icon kullanınız.")
    is_active = models.BooleanField(default=True, verbose_name = "Aktif mi?", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Sosyal Medya"