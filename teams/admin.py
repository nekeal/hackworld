from django.contrib import admin
from .models import Team
# Register your models here.


class TeamAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return Team.objects.filters(teamleader=request.user.participant)
admin.site.register(Team)