from django.shortcuts import render
from django.core.paginator import Paginator
from django.conf import settings
from django.utils import translation
from django.http import HttpResponseRedirect
from django.urls import reverse, resolve
from django.urls.exceptions import Resolver404
from django.utils.translation import get_language
from urllib.parse import urlparse
from blog.models import Blog
from .models import (
    HomeSlider, IslamCondition, 
    StatisticInfo, Statistic, 
    Galery
)

def index(request):
    user_language = get_language()
    sliders = HomeSlider.objects.order_by('-created_at').all()
    last_4_statistics = Statistic.objects.order_by('-created_at').all()[:4]
    statistic_info = StatisticInfo.objects.order_by('-created_at').first()
    last_3_blogs = Blog.objects.filter(category__language=user_language).order_by('-created_at')[:3]
    
    context = {
        'sliders': sliders,
        'statistics': last_4_statistics,
        'statistic_info': statistic_info,
        'last_3_blogs' : last_3_blogs,
    }
    
    return render(request, 'base/index.html', context)

def about(request):
    conditions = IslamCondition.objects.order_by('-created_at').all()
    context = {
        'conditions': conditions,
    }
    return render(request, 'base/about.html', context)


def galeries(request):
    galeries = Galery.objects.order_by('-created_at').all()
    paginator = Paginator(galeries, 18)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'galeries': galeries,
        'page_obj' : page_obj,
    }
    
    return render(request, 'base/galery.html', context)



def set_language(request, language):
    if language not in dict(settings.LANGUAGES):
        return HttpResponseRedirect("/")

    referer = request.META.get("HTTP_REFERER", "/")
    try:
        view = resolve(urlparse(referer).path)
        translation.activate(language)
        app_name = view.app_name if hasattr(view, 'app_name') else None
        view_name = f"{app_name}:{view.url_name}" if app_name else view.url_name

        response = HttpResponseRedirect(
            reverse(view_name, args=view.args, kwargs=view.kwargs)
        )
    except Resolver404:
        response = HttpResponseRedirect("/")
    
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response