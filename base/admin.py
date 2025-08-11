from django.contrib import admin
from .models import (
    GeneralItem, HomeSlider, About, 
    IslamCondition, Statistic, StatisticInfo,
    Subscribe, Galery, PageBanner, MetaTag,
    NavbarItem, DynamicPage, SocialMedia,
)
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin
from django.conf import settings
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

@admin.register(GeneralItem)
class GeneralItemAdmin(TabbedTranslationAdmin):
    list_display = ('title',)
    group_fieldsets = True    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(NavbarItem)
class NavbarItemAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'url', 'order', 'is_active', 'position')
    
    group_fieldsets = True    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    
    
@admin.register(HomeSlider)
class HomeSliderAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'image',)
    group_fieldsets = True    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    
@admin.register(About)
class AboutAdmin(TabbedTranslationAdmin):
    list_display = ('title',)
    group_fieldsets = True    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    
    
@admin.register(IslamCondition)
class IslamConditionAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'image',)
    group_fieldsets = True    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    
    
@admin.register(Statistic)
class StatisticAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'value',)
    group_fieldsets = True    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    
    
@admin.register(StatisticInfo)
class StatisticInfoAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'image',)
    group_fieldsets = True    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    
    
@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    

@admin.register(Galery)
class GaleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    
    
@admin.register(PageBanner)
class PageBannerAdmin(TabbedTranslationAdmin):
    list_display = ('page', 'title', 'image')
    group_fieldsets = True    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
    
@admin.register(MetaTag)
class MetaTagAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'name', 'slug',)
    search_fields = ('page_name', 'name', 'content')


@admin.register(DynamicPage)
class DynamicPageAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'slug', 'banner_img', 'created_at')
    group_fieldsets = True    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    
    
@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'icon', 'is_active')