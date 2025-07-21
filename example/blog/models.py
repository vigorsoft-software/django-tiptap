from django.db import models
from django_tiptap.fields import TipTapField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = TipTapField()

    def __str__(self):
        return self.title
