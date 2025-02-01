from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Service
from base.models import Subscribe
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

@receiver(post_save, sender=Service)
def send_service_notification(sender, instance, created, **kwargs):
    if created:
        subject = f"Yeni bir servis eklendi: {instance.title}"
        message = render_to_string('base/service_message.html', { 'instance': instance })
        from_email = 'metin.qardasov2003@gmail.com'
        recipient_list = Subscribe.objects.values_list('email', flat=True)
        
        if recipient_list:
            email = EmailMessage(subject, message, from_email, bcc=list(recipient_list))
            email.content_subtype = "html"
            email.send(fail_silently=False)