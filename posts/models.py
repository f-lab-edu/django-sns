from django.db import models

from common.models import CommonModel


# Create your models here.
class Post(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="posts",
    )
    content = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.user}: {self.content}"