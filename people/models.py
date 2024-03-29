from django.db import models
from django.core.validators import ValidationError
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.shortcuts import reverse
# Create your models here.

def advance_level_validator(value):
    if value < 1 or value > 10:
        raise ValidationError("Provide number between 1 and 10")

def get_user():
    return User.objects.first().id

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


class Skill(models.Model):
    name            = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ParticipantSkill(models.Model):
    skill            = models.ForeignKey(Skill, on_delete=models.CASCADE)
    advanced_level  = models. SmallIntegerField(validators=[advance_level_validator,], default=1)
    participant     = models.ForeignKey('Participant', on_delete=models.CASCADE)

    def __str__(self):
        return  self.skill.name

class Participant(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name                = models.CharField(max_length=50)
    surname             = models.CharField(max_length=50)
    city                = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    short_description   = models.CharField(max_length=100, blank=True)
    description         = models.TextField(blank=True)
    linkedin_url        = models.URLField(blank=True)
    github_url          = models.URLField(blank=True)
    # email       = models.EmailField()
    # skills      = models.ManyToManyField(ParticipantSkill, blank=True, related_name='participants')

    def __str__(self):
        return f"{self.name} {self.surname}"

    def get_absolute_url(self):
        return reverse('people:alien-profile', args=(self.id,))




@receiver(post_delete, sender=Participant)
def auto_delete_user(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()