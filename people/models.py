from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)

class Participant(models.Model):
    name        = models.CharField(max_length=50)
    surname     = models.CharField(max_length=50)
    city        = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)