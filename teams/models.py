from django.db import models
from people.models import Participant
from hackathon.models import Hackathon
# Create your models here.


class Team(models.Model):
    name        = models.CharField(max_length=100)
    members     = models.ManyToManyField(Participant, related_name='teams')
    teamleader  = models.ForeignKey(Participant, on_delete=models.SET_NULL, null=True, blank=True, related_name='my_teams')
    looking_for = models.BooleanField()
    hackathon   = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    candidates  = models.ManyToManyField(Participant, blank=True)