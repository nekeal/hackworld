from django.db import models
from django.core.validators import ValidationError
# Create your models here.

def advance_level_validator(value):
    if value < 1 or value > 10:
        raise ValidationError("Provide number between 1 and 10")

class City(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


class Skill(models.Model):
    name            = models.CharField(max_length=50)

class ParticipantSkill(models.Model):
    name            = models.ForeignKey(max_length=50)
    advanced_level  = models. SmallIntegerField(validators=[advance_level_validator,])

class Participant(models.Model):
    name        = models.CharField(max_length=50)
    surname     = models.CharField(max_length=50)
    city        = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    email       = models.EmailField()
    skills      = models.ManyToManyField(ParticipantSkill)