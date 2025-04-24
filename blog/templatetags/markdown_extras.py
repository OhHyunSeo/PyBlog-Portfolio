from django import template
from django.template.defaultfilters import stringfilter
import markdown

register = template.Library()

@register.filter
@stringfilter
def markdown_to_html(value):
    return markdown.markdown(value, extensions=['markdown.extensions.fenced_code', 'markdown.extensions.tables']) 