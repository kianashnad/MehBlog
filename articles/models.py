from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  # Stores Markup
    amount_like = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
