from django.contrib import admin
from .models import Participant, City, Skill, ParticipantSkill
# Register your models here.

admin.site.register(Participant)
admin.site.register(City)
admin.site.register(Skill)
admin.site.register(ParticipantSkill)