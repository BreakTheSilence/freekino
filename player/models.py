from django.db import models


class Films(models.Model):
    title = models.CharField(max_length=120)
    link = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title
