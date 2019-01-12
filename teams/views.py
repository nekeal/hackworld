from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import JsonResponse
from .models import Team
from people.models import Participant
from django.core.mail import send_mail
from django.views import View
from hackworld.settings.base import EMAIL_HOST_USER

class TeamListView(ListView):
    model = Team
    template_name = 'teams/team-list.html'


class TeamJoinRequestNotifier(View):
    def post(self, request):
        team_id = self.request.POST.get('team-id', self.request.GET.get('team-id'))
        try:
            team_id = int(team_id)
        except Exception:
            return JsonResponse({'success': False, 'message': f'Invalid format POST={self.request.POST} GET={request.GET} method={request.method}'})
        participant = Participant.objects.get(user=request.user)
        team = Team.objects.filter(id=team_id)
        if team.count() == 0:
            return JsonResponse({'success': False, 'message': f'No team with id={team_id}'})
        team = team.first()
        if team.members.count() >= team.hackathon.max_size:
            return JsonResponse({'success': False, 'message': f'Team is already full'})
        if team.members.filter(user=participant.user):
            return JsonResponse({'success': False, 'message': f'You are already in this team'})

        send_mail(
            'Team join request',
            f'User {participant} wants to join your team {team.name}.',
            EMAIL_HOST_USER,
            [team.teamleader.email]
        )
        return JsonResponse({'success': True, 'message': 'Mail sent'})

