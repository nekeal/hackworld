from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import JsonResponse
from .models import Team
from people.models import Participant
from django.core.mail import send_mail

class TeamListView(ListView):
    model = Team
    template_name = 'teams/team-list.html'


def notify_teamleader(request):
    id = request.POST['team-id']
    participant = Participant.objects.get(request.user)
    team = Team.objects.filter(id=id)
    if team.count() == 0:
        return JsonResponse({'success': False, 'message': f'No team with id={id}'})
    team = team.first()
    if team.members.all().count() < 5:
        return JsonResponse({'success': False, 'message': f'Team is already full'})
    # if team.members.all()


    send_mail(team.teamleader)


