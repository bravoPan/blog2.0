from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=True)
def cut_avatar_name(value):
    # print(value)
    return value[1:]
