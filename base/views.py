from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    HomeSlider, IslamCondition, 
    StatisticInfo, Statistic, 
    Galery, DynamicPage
)
from django.core.paginator import Paginator

def index(request):
    
    sliders = HomeSlider.objects.order_by('-created_at').all()
    last_4_statistics = Statistic.objects.order_by('-created_at').all()[:4]
    statistic_info = StatisticInfo.objects.order_by('-created_at').first()
    
    context = {
        'sliders': sliders,
        'statistics': last_4_statistics,
        'statistic_info': statistic_info,
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


def error(request):
    return render(request, 'base/404.html')