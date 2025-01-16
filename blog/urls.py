from django.urls import path
from .views import blogs, blog_detail

app_name = 'blog'

urlpatterns = [
    path('', blogs, name='blogs'),
    path('<slug:blog_slug>/', blog_detail, name='blog_detail'),
]