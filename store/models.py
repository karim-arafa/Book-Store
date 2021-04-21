from django.db import models


class Store(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField(max_length=2048, null=True, blank=True)

    def __str__(self):
        return self.title