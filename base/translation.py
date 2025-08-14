from modeltranslation.translator import TranslationOptions,register
from .models import (
    GeneralItem, HomeSlider, About, 
    IslamCondition, Statistic, StatisticInfo,
    Galery, PageBanner, MetaTag,
    NavbarItem, DynamicPage
)

@register(GeneralItem)
class GeneralItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    

@register(HomeSlider)
class HomeSliderTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    
    
@register(IslamCondition)
class IslamConditionTranslationOptions(TranslationOptions):
    fields = ('title',)
    

@register(StatisticInfo)
class StatisticInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    

@register(Statistic)
class StatisticTranslationOptions(TranslationOptions):
    fields = ('title',)
    
    
@register(PageBanner)
class PageBannerTranslationOptions(TranslationOptions):
    fields = ('title',)
    

@register(NavbarItem)
class NavbarItemTranslationOptions(TranslationOptions):
    fields = ('title',)
    

@register(DynamicPage)
class DynamicPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
    
