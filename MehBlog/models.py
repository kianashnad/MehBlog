from django.db import models


class BaseModel(models.Model):
    """
    An abstract base class including base fields like created_at and updated_at.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
