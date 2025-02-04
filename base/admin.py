from django.contrib import admin
from .models import (
    GeneralItem, HomeSlider, About, 
    IslamCondition, Statistic, StatisticInfo,
    Subscribe, Galery, PageBunner
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