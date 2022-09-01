from django.db import models

# Create your models here.


class Gallery(models.Model):
    picture = models.CharField(max_length=2000)
    title = models.CharField(max_length=2000)
    link = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return self.title
