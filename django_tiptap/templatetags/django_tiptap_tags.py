from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from ..conf import get_plugin_urls

register = template.Library()


@register.simple_tag
def tiptap_resources():
    """Return script tags to include Tiptap."""
    src = static("django_tiptap/js/tiptap-init.js")
    tags = [f'<script src="{url}"></script>' for url in get_plugin_urls()]
    tags.append(f'<script src="{src}"></script>')
    return mark_safe("".join(tags))
