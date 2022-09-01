from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=2000)
    theme = models.CharField(max_length=2000)
    content1 = models.CharField(max_length=200000)
    content2 = models.CharField(max_length=200000)
    timestamp = models.DateTimeField(auto_now_add=True)
    map_code = models.CharField(max_length=2000)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    sermons_theme = models.CharField(max_length=2000)
    sermon_location = models.CharField(max_length=2000)
    # Comment

    def __str__(self):
        return self.title + self.theme
