from .models import (
    GeneralItem, About, PageBunner
)
from django.contrib import messages
from service.models import Service
from blog.models import Blog
from django.shortcuts import redirect
from .forms import SubscribeForm

def site_settings(request):
    
    form = SubscribeForm(request.POST or None)
    page_id = request.GET.get('page_id')
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Başarıyla abone olundu!!!")
    
    general_item = GeneralItem.objects.first()
    about = About.objects.first()
    last_3_services = Service.objects.all().order_by('-created_at')[:3]
    last_6_services = Service.objects.all().order_by('-created_at')[:6]
    last_3_blogs = Blog.objects.all().order_by('-created_at')[:3]
    page_bunner = PageBunner.objects.first()
    
    context = {
        'item' : general_item,
        'about' : about,
        'last_3_services' : last_3_services,
        'form' : form,
        'last_6_services' : last_6_services,
        'last_3_blogs' : last_3_blogs,
        'bunner' : page_bunner
    }
    
    return context