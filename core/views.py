from django.shortcuts import get_object_or_404, render
from base.models import DynamicPage


def dynamic_page_view(request, slug):
    page = get_object_or_404(DynamicPage, slug=slug)
    context = {
        'page': page
    }
    return render(request, 'base/dynamic_page.html', context)