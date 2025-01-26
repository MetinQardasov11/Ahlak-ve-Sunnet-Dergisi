from django.contrib import admin
from .models import SocialTag, MetaTags

@admin.register(SocialTag)
class SocialTagAdmin(admin.ModelAdmin):
    list_display = ('tag_type', 'template_page', 'is_active',)
    list_filter = ('tag_type', 'is_active')
    
    
@admin.register(MetaTags)
class MetaTagsAdmin(admin.ModelAdmin):
    list_display = ('tag_type', 'page', 'is_active')
    list_filter = ('tag_type', 'is_active')
    search_fields = ('content', 'page__template_name',)