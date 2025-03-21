from django.contrib.auth.models import AbstractUser
from django.db import models

from common.models import CommonModel


# Create your models here.
class User(AbstractUser, CommonModel):

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    first_name = models.CharField(
        max_length=150,
        editable=True,
    )
    last_name = models.CharField(
        max_length=150,
        editable=True,
    )
    name = models.CharField(max_length=150,)
    avatar = models.ImageField(blank=True,)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
    bio = models.TextField(blank=True)
