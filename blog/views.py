from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Blog, BlogCategory
from django.utils.translation import get_language


def blogs(request):
    selected_category_slug = request.GET.get('category', None)
    user_language = get_language()
    categories = BlogCategory.objects.filter(language=user_language, is_active=True)
    blogs = Blog.objects.filter(category__language=user_language).order_by('-created_at')
    selected_category_obj = None

    if selected_category_slug:
        selected_category_obj = categories.filter(slug=selected_category_slug).first()
        if selected_category_obj:
            blogs = blogs.filter(category=selected_category_obj)

    paginator = Paginator(blogs, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': selected_category_slug,
        'selected_category_obj': selected_category_obj
    }

    return render(request, 'blog/blogs.html', context)



def blog_detail(request, blog_slug):
    user_language = get_language()
    
    try:
        blog = Blog.objects.get(slug=blog_slug, language=user_language)
    except Blog.DoesNotExist:
        return redirect('base:error')
    
    context = {
        'blog' : blog,
    }
    
    return render(request, 'blog/blog-details.html', context)