from django.shortcuts import render, get_object_or_404
from .models import Service
from django.core.paginator import Paginator


def services(request):
    services = Service.objects.all().order_by('-created_at')
    paginator = Paginator(services, 9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'services' : services,
        'page_obj' : page_obj,
    }    

    return render(request, 'service/services.html', context)


def service_detail(request, service_slug):
    services = Service.objects.all().order_by('-created_at')
    service = get_object_or_404(Service, slug = service_slug)
    
    context = {
        'service' : service,
        'services' : services,
    }
    
    return render(request, 'service/service-details.html', context)