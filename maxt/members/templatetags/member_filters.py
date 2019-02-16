from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter('active_page_class')
def active_page_class(value, page):
    if page == "/": # Special case "/" because every page starts with "/"
        if value == "/":
            return mark_safe('class="active"')
        return ""

    if value.startswith(page):
        return mark_safe('class="active" ')
    return ""
