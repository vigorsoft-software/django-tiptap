from django.db import models

from .widgets import TipTapWidget


class TipTapField(models.TextField):
    """TextField that uses TipTapWidget by default."""

    def formfield(self, **kwargs):
        defaults = {"widget": TipTapWidget}
        defaults.update(kwargs)
        return super().formfield(**defaults)
