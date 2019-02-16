from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter('active_page_class')
def active_page_class(value, page):
    if value == "/" and page == "/":
        return mark_safe('class="active" ')
    if page == "/": # because every page starts with "/"
        return ""
    if value.startswith(page):
        return mark_safe('class="active" ')
    return ""
