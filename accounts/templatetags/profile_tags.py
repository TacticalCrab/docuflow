from django.contrib.auth.models import AbstractUser
from django import template

register = template.Library()

@register.filter
def get_user_profile_fields(user: AbstractUser):
    fields = ['username', 'email', 'first_name', 'last_name']

    return [
        {
            "label": user._meta.get_field(f).verbose_name.capitalize(),
            "value": getattr(user, f)
        }
        for f in fields
    ]