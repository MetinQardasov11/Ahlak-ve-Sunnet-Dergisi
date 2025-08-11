from django.contrib import admin
from .models import Blog, BlogImage, BlogCategory
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationStackedInline

@admin.register(BlogCategory)
class BlogCategoryAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'language', 'is_active', 'slug',)
    list_filter = ('language',)
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    
    
@admin.register(Blog)
class BlogAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'category', 'slug')
    list_filter = ('category',)
    inlines = [BlogImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    