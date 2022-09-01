from django.db import models

# Create your models here.


class Sermon(models.Model):

    title = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)
    # pastor_name
    # pastor_picture
    ICONS = (
        ("heart", "heart"),
        ("heart", "heart"),
        ("heart", "heart"),
    )
    audio = models.CharField(max_length=2000)
    article = models.CharField(max_length=2000)
    audio_duration = models.CharField(max_length=2000)
    Icon = models.CharField(max_length=2000, choices=ICONS)

    def __str__(self) -> str:
        return self.title
