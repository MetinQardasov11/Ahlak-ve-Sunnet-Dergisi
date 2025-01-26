from django import template
from django.template.defaulttags import register
from base.models import TemplatePage
from seo.models import MetaTags, SocialTag

register = template.Library()

@register.simple_tag
def get_metatags_data(page_name, path=None):
    page_name = path if not page_name else page_name
    meta_tags = MetaTags.objects.filter(is_active=True, page=page_name).all()
    return meta_tags if meta_tags else MetaTags.objects.filter(is_active=True, page=None).all()


@register.simple_tag
def get_socialtags_data(page_name, path=None):
    page_name = path if not page_name else page_name
    social_tags = SocialTag.objects.filter(is_active=True, template_page=page_name).all()
    return social_tags if social_tags else SocialTag.objects.filter(is_active=True, template_page=None).all()