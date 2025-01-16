from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog


def blogs(request):
    
    blogs = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blogs, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'blogs' : blogs,
        'page_obj' : page_obj,
    }  
    
    return render(request, 'blog/blogs.html', context)



def blog_detail(request, blog_slug):
    
    blog = get_object_or_404(Blog, slug=blog_slug)
    context = {
        'blog' : blog,
    }
    
    return render(request, 'blog/blog-details.html', context)