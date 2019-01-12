from django.db import models

# Create your models here.


class Hackathon(models.Model):
    name                = models.CharField(max_length=100)
    official_website    = models.URLField()
    accepted            = models.BooleanField(default=False)
    descprition         = models.TextField()
    proof               = models.TextField(help_text='Put here any information about hackathon and optional links to facebook'
                                                     'event or official website ')