from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from .models import DynamicPage, NavbarItem

@receiver(post_save, sender=DynamicPage)
def create_navbar_item(sender, instance, created, **kwargs):
    if created:
        max_order = NavbarItem.objects.aggregate(max_order=models.Max('order'))['max_order']
        new_order = (max_order + 1) if max_order is not None else 1
        
        NavbarItem.objects.create(
            title=instance.title,
            url=f"/{instance.slug}",
            position='navbar',
            order=new_order,
            is_active=False
        )