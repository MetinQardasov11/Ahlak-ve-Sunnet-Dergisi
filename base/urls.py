from django.urls import path
from .views import index, about, galeries, error

app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
    path('hakkimizda/', about, name='about'),
    path('galeri/', galeries, name='galeries'),
    path('hata/', error, name='error'),
]