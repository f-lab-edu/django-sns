from django.db import models

# Create your models here.
# Abstract Models
class CommonModel(models.Model):
    """ Common model definition"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
