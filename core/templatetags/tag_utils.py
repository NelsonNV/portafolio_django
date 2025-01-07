
from django import template

register = template.Library()

@register.filter
def get_attr(instance, attr_name):
    return getattr(instance, attr_name, None)
