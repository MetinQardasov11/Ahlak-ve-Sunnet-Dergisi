from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Blog Başlığı')
    description = RichTextField(verbose_name='Açıklama')
    image = models.ImageField(verbose_name='Blog Resmi')
    author = models.CharField(max_length=100, verbose_name='Blog Yazarı')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name='Slug', editable=False)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Bloglar'
        
        
class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images', verbose_name = "Blog")
    image = models.ImageField(upload_to='blog_img', verbose_name = "Resim", null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return f"{self.blog.title} - Image {self.id}"
    
    class Meta:
        verbose_name_plural = "Blog Alt Resimleri"