from django.db import models

# Create your models here.


class BaseModel(models.Model):
    unlisted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
