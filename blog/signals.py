from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.utils.text import slugify
from .models import Blog
from base.models import Subscribe
from django.template.loader import render_to_string
from premailer import transform

@receiver(post_save, sender=Blog)
def send_blog_notification(sender, instance, created, **kwargs):
    if created:
        subject = f"Yeni bir blog yayınlandı: {instance.title}"
        message = render_to_string('base/message.html', { 'instance': instance })

        from_email = 'metin.qardasov2003@gmail.com'
        recipient_list = Subscribe.objects.values_list('email', flat=True)

        if recipient_list:
            email = EmailMessage(subject, message, from_email, bcc=list(recipient_list))
            email.content_subtype = "html"
            email.send(fail_silently=False)