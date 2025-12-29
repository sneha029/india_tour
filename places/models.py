from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    best_time = models.CharField(max_length=100)
    image_url = models.URLField(max_length=10000)
    quote = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
