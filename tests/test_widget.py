import unittest
import django
from django.conf import settings

from django_tiptap.widgets import TipTapWidget


class WidgetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not settings.configured:
            settings.configure(
                INSTALLED_APPS=['django.contrib.staticfiles', 'django_tiptap'],
                STATIC_URL='/static/',
            )
        django.setup()
        super().setUpClass()

    def test_media(self):
        widget = TipTapWidget()
        media = str(widget.media)
        self.assertIn('tiptap', media)

if __name__ == '__main__':
    unittest.main()
