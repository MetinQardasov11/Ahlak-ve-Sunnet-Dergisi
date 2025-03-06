from django.contrib import admin
from .models import Blog, BlogImage, BlogCategory
from modeltranslation.admin import TranslationAdmin

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'is_active', 'slug',)
    list_filter = ('language',)


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug')
    list_filter = ('category',)
    inlines = [BlogImageInline]