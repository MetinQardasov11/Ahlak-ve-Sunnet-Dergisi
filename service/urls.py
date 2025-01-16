from django.urls import path
from .views import services, service_detail

app_name = 'service'

urlpatterns = [
    path('', services, name='services'),
    path('<slug:service_slug>/', service_detail, name='service_detail'),
]