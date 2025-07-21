from django import forms
from django.utils.safestring import mark_safe

from .conf import get_plugin_urls


class TipTapWidget(forms.Textarea):
    template_name = "django_tiptap/widget.html"

    @property
    def media(self):
        js = get_plugin_urls() + ["django_tiptap/js/tiptap-init.js"]
        return forms.Media(js=js)

    def format_value(self, value):
        return value or ""

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        return mark_safe(html)
