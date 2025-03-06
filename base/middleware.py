from django.utils.translation import get_language
from django.shortcuts import render
from .models import NavbarItem

class TranslationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        current_language = get_language()
        title_field = f"title_{current_language}"

        path_segments = request.path.strip("/").split("/")
        if len(path_segments) > 1:
            route = path_segments[1]
        else:
            route = path_segments[0]

        if NavbarItem.objects.filter(url=f"/{route}/").exists():
            navbar_item = NavbarItem.objects.get(url=f"/{route}/")
            if not getattr(navbar_item, title_field, None):
                return render(request, "base/404.html", status=404)

        return response