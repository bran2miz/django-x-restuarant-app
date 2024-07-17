from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Location(models.Model):
    location = models.CharField(max_length=64)
    description = models.TextField(default="")
    traveler = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('locations_detail', args=[str(self.id)])