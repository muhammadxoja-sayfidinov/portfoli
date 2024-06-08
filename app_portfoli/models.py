from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.JSONField()  # List of image URLs
    link = models.URLField()

    def __str__(self):
        return self.name
