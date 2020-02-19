from django.contrib.auth import get_user_model
from django.db import models

from MehBlog.models import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()  # Stores Markup
    amount_like = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title


class Like(BaseModel):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
