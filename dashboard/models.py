from django.db import models


class About(models.Model):
    content = models.TextField(max_length=200000, null=True)
    picture1 = models.TextField(max_length=2000, null=True)
    picture2 = models.TextField(max_length=2000, null=True)

    def __str__(self):
        return self.content
