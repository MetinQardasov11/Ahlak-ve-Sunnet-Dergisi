from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import index, about, galeries, set_language

app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
    path('hakkimizda/', about, name='about'),
    path('galeri/', galeries, name='galeries'),
    path("set_language/<str:language>", set_language, name="set-language"),
]