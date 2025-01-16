from django.urls import path
from .views import index, about, galeries, error

app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('galeries/', galeries, name='galeries'),
    path('error/', error, name='error'),
]