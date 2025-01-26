from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from PIL import Image

class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="Servis Başlığı")
    description = RichTextField(verbose_name = "Açıklama")
    image = models.ImageField(upload_to='service_img', verbose_name = "Resim")
    slug = models.SlugField(null=True, blank=True, editable=False, verbose_name="Slug")

    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")
    
    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Servisler"
    
    
class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images', verbose_name = "Servis")
    image = models.ImageField(upload_to='service_img', verbose_name = "Resim", null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return f"{self.service.title} - Image {self.id}"
    
    class Meta:
        verbose_name_plural = "Servis Alt Resimleri"