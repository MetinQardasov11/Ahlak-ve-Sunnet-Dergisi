from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.utils.text import slugify
from .models import Blog
from base.models import Subscribe

@receiver(post_save, sender=Blog)
def send_blog_notification(sender, instance, created, **kwargs):
    if created:
        subject = f"Yeni bir blog yayınlandı: {instance.title}"
        message = (
            f"Merhaba,\n\n"
            f"'{instance.title}' başlıklı yeni bir blog sitemize eklenmiştir. "
            f"Detaylı bilgi için lütfen sitemizi ziyaret edin.\n\n"
            f"Teşekkürler!"
        )
        from_email = 'metin.qardasov2003@gmail.com'
        recipient_list = Subscribe.objects.values_list('email', flat=True)

        if recipient_list:
            email = EmailMessage(subject, message, from_email, bcc=list(recipient_list))
            email.send(fail_silently=False)
