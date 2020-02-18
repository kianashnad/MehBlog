from django.contrib.auth import get_user_model
from django.db import models

from MehBlog.models import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()  # Stores Markup
    amount_like = models.IntegerField()


class Like(BaseModel):
    sender = get_user_model()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
