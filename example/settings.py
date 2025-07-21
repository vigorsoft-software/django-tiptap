SECRET_KEY = 'dummy'
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django_tiptap',
    'example.blog',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
STATIC_URL = '/static/'
ROOT_URLCONF = 'example.urls'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
