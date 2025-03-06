from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='İsim Soyisim')
    email = models.EmailField(verbose_name='Email adresi')
    phone = models.CharField(max_length=50, verbose_name='Telefon Numarası')
    subject = models.CharField(max_length=300, verbose_name='Mesajın Konusu')
    message = models.TextField(verbose_name='Mesajın metni')
    is_reply = models.BooleanField(default=False, verbose_name='Cevaplandı mı?', null=True, blank=True)
    created_at = models.DateField(verbose_name="Mesajın geliş tarihi", auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'İletişim'
        
        
class Address(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Adres Başlığı", null=True, blank=True)
    address = models.TextField(verbose_name = "Adres", null=True, blank=True)
    map = models.URLField(verbose_name = "Harita Linki", max_length=600, null=True, blank=True)
    work_time = models.CharField(verbose_name="Açılıp kapanma saatleri", max_length=200, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Adresler"
    
    
class Email(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Email Başlığı", null=True, blank=True)
    email = models.EmailField(verbose_name = "Email", null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = "Mailler"
    
    
class Phone(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Telefon Başlığı", null=True, blank=True)
    phone = models.CharField(max_length=200, verbose_name = "Telefon", null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name_plural = "Telefon Numraları"
