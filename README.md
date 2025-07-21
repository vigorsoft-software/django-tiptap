# Django TipTap

Django TipTap provides a simple integration of the [Tiptap](https://tiptap.dev/) editor with Django 5+. It exposes a form widget and model field that can be added to your apps with minimal configuration.

## Installation

Install from PyPI:

```bash
pip install django-tiptap
```

Or install directly from GitHub using `poetry`:

```bash
poetry add git+https://github.com/example/django-tiptap.git
```

Add `django_tiptap` to your `INSTALLED_APPS` and collect static files.

```python
from django.db import models
from django_tiptap.fields import TipTapField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = TipTapField()
```

Include the widget in admin or custom forms:

```python
from django import forms
from django_tiptap.widgets import TipTapWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {"content": TipTapWidget()}
```

Add the required media in your template using the provided template tag:

```django
{% load django_tiptap_tags %}
{% tiptap_resources %}
```

### Plugin configuration

All known TipTap plugins are loaded by default. To override the list, define
`DJANGO_TIPTAP_PLUGINS` and optional `DJANGO_TIPTAP_PLUGIN_URLS` in your Django
settings:

```python
DJANGO_TIPTAP_PLUGINS = ["core", "starter-kit"]
DJANGO_TIPTAP_PLUGIN_URLS = {
    "underline": "https://unpkg.com/@tiptap/extension-underline@2/dist/tiptap-extension-underline.umd.js",
}
```

The example project under `example/` demonstrates a minimal integration.

Read the full documentation at [Read the Docs](https://django-tiptap.readthedocs.io/).
