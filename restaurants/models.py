from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default="")
    foodie = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurants_detail', args=[str(self.id)])