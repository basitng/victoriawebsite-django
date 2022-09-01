from django.db import models

# Create your models here.


class Ministry(models.Model):
    picture = models.CharField(max_length=2000)
    title = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
    # pastor reference (name,avatar)
