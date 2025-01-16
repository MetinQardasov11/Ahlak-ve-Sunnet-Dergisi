from django.contrib import admin
from .models import (
    GeneralItem, HomeSlider, About, 
    IslamCondition, Statistic, StatisticInfo,
    Subscribe, Galery, PageBunner, SEOModel
)

@admin.register(GeneralItem)
class GeneralItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'nav_img', 'footer_img', 'favicon_img',)

    
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
    
    
@admin.register(PageBunner)
class PageBunnerAdmin(admin.ModelAdmin):
    list_display = ('title', )
    

@admin.register(SEOModel)
class SEOModelAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at", "slug")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "description", "keywords")
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)
    fields = ("title", "description", "keywords", "image", "slug", "twitter_handle")
    readonly_fields = ("created_at", "updated_at")