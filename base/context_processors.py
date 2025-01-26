from .models import (
    GeneralItem, About, PageBunner
)
from django.contrib import messages
from service.models import Service
from blog.models import Blog
from django.shortcuts import redirect
from .forms import SubscribeForm
from seo.models import MetaTags, SocialTag


def site_settings(request):
    
    form = SubscribeForm(request.POST or None)
    page_id = request.GET.get('page_id')
    
    if page_id:
        meta_tags = MetaTags.objects.filter(page_id=page_id, is_active=True)
        social_tags = SocialTag.objects.filter(template_page_id=page_id, is_active=True)
    else:
        meta_tags = []
        social_tags = []
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Başarıyla abone olundu!!!")
    
    general_item = GeneralItem.objects.first()
    about = About.objects.first()
    last_3_services = Service.objects.all().order_by('-created_at')[:3]
    last_5_services = Service.objects.all().order_by('created_at')
    last_3_blogs = Blog.objects.all().order_by('-created_at')[:3]
    page_bunner = PageBunner.objects.first()
    
    context = {
        'item' : general_item,
        'about' : about,
        'last_3_services' : last_3_services,
        'form' : form,
        'last_5_services' : last_5_services,
        'last_3_blogs' : last_3_blogs,
        'bunner' : page_bunner,
        'tags': meta_tags,
        'social_tags': social_tags,
    }
    
    return context