from django import template
from django.utils.translation import get_language

register = template.Library()

@register.filter
def remove(value, arg):
    return [x for x in value if x != arg]

@register.filter
def get_translated_content(meta_tag, lang_code=None):
    if not lang_code:
        lang_code = get_language()

    print(lang_code)
    
    translated_content = getattr(meta_tag, f"content_{lang_code}", meta_tag.content)
    print(translated_content)
    return translated_content or meta_tag.content