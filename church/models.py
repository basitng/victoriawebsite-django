from django.db import models


class Church(models.Model):

    name = models.CharField(max_length=2000)
    phone = models.CharField(max_length=2000)
    email = models.EmailField()
    website = models.CharField(max_length=2000)
    venue = models.CharField(max_length=2000)
    support_phone = models.CharField(max_length=2000)
    support_email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Church"
