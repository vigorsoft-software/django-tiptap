from django.conf import settings

# Default plugin URL mapping using unpkg CDN
DEFAULT_PLUGIN_URLS = {
    "core": "https://unpkg.com/@tiptap/core@2/dist/tiptap-core.umd.js",
    "starter-kit": "https://unpkg.com/@tiptap/starter-kit@2/dist/tiptap-starter-kit.umd.js",
    # extend with more plugins as needed
}


def get_plugin_urls():
    """Return the list of plugin URLs based on settings."""
    extra = getattr(settings, "DJANGO_TIPTAP_PLUGIN_URLS", {})
    plugins = DEFAULT_PLUGIN_URLS.copy()
    plugins.update(extra)
    enabled = getattr(settings, "DJANGO_TIPTAP_PLUGINS", list(plugins.keys()))
    urls = []
    for name in enabled:
        url = plugins.get(name, name)
        urls.append(url)
    return urls
