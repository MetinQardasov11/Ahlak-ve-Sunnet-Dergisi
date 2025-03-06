from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import (
    index, about, 
    galeries, error,
    set_language
)

from video.views import video_not_found
app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
    path('hakkimizda/', about, name='about'),
    path('galeri/', galeries, name='galeries'),
    path('hata/', error, name='error'),
    path('not-found/', video_not_found, name='video_not_found'),
    path("set_language/<str:language>", set_language, name="set-language"),
]