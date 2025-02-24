from django.contrib import admin
from .models import (
    GeneralItem, HomeSlider, About, 
    IslamCondition, Statistic, StatisticInfo,
    Subscribe, Galery, PageBanner, MetaTag,
    NavbarItem, DynamicPage, SocialMedia
)

@admin.register(GeneralItem)
class GeneralItemAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(NavbarItem)
class NavbarItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order', 'is_active', 'position')
    
    
@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
    
@admin.register(IslamCondition)
class IslamConditionAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    
    
@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('title', 'value',)
    
    
@admin.register(StatisticInfo)
class StatisticInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    
    
@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    

@admin.register(Galery)
class GaleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    
    
@admin.register(PageBanner)
class PageBannerAdmin(admin.ModelAdmin):
    list_display = ('page', 'title', 'image')
    
@admin.register(MetaTag)
class MetaTagAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'name', 'slug',)
    search_fields = ('page_name', 'name', 'content')
    
@admin.register(DynamicPage)
class DynamicPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'banner_img', 'created_at')
    
    
@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'icon', 'is_active')