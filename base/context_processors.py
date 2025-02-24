from .models import (
    GeneralItem, About, 
    PageBanner, MetaTag, 
    NavbarItem, DynamicPage,
    SocialMedia
)
from django.contrib import messages
from service.models import Service
from blog.models import Blog
from django.shortcuts import redirect
from .forms import SubscribeForm

def site_settings(request):
    form = SubscribeForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Başarıyla abone olundu!!!")
    
    general_item = GeneralItem.objects.first()
    about = About.objects.first()
    last_3_services = Service.objects.all().order_by('-created_at')[:3]
    last_6_services = Service.objects.all().order_by('-created_at')[:6]
    last_3_blogs = Blog.objects.all().order_by('-created_at')[:3]
    page_bunner = PageBanner.objects.first()
    page_slug = request.path.strip("/").split("/")[0]
    social_medias = SocialMedia.objects.filter(is_active=True)
    
    if not page_slug:
        page_slug = ""
    
    meta_tags = MetaTag.objects.filter(slug=page_slug)
    og_tags = [tag for tag in meta_tags if tag.name.startswith("og:")]
    twitter_tags = [tag for tag in meta_tags if tag.name.startswith("twitter:")]
    other_tags = [tag for tag in meta_tags if not tag.name.startswith(("og:", "twitter:"))]
    
    navbar_items = NavbarItem.objects.filter(is_active=True).filter(position__in=['both', 'navbar']).order_by('order')
    footer_items = NavbarItem.objects.filter(is_active=True).filter(position__in=['both', 'footer']).order_by('order')
    
    banners = { banner.page: {'title': banner.title, 'image': banner.image.url if banner.image else None} for banner in PageBanner.objects.all() }
    dynamic_pages = DynamicPage.objects.all()
    
    context = {
        'item' : general_item,
        'about' : about,
        'last_3_services' : last_3_services,
        'form' : form,
        'last_6_services' : last_6_services,
        'last_3_blogs' : last_3_blogs,
        'bunner' : page_bunner,
        'og_tags': og_tags,
        'twitter_tags': twitter_tags,
        'other_tags': other_tags,
        'navbar_items': navbar_items,
        'footer_items': footer_items,
        'banners': banners,
        'dynamic_pages': dynamic_pages,
        'social_medias': social_medias,
    }
    
    return context