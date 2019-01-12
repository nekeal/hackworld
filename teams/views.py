from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Team


class TeamListView(ListView):
    model = Team
    template_name = 'teams/team-list.html'
