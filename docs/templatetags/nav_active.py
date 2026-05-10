from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def is_active(context, url_name, **kwargs):
    request = context.get('request')
    if not request:
        return ""
    
    try:
        target_url = reverse(url_name, kwargs=kwargs)
        if request.path == target_url:
            return "active"
    except:
        pass
    
    return ""