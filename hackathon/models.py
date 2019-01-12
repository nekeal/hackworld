from django.db import models
from django.contrib.auth.models import User

from people.models import get_user
# Create your models here.


class Hackathon(models.Model):
    name                = models.CharField(max_length=100)
    official_website    = models.URLField(blank=True)
    accepted            = models.BooleanField(default=False)
    descprition         = models.TextField()
    proof               = models.TextField(help_text='Put here any information about hackathon and optional links to facebook'
                                                     'event or official website ')
    added_by            = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=get_user)

    def __str__(self):
        return self.name
