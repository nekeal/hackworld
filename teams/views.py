from django.shortcuts import render, redirect, reverse
from django.views.generic.list import ListView
from django.http import JsonResponse
from .models import Team
from .forms import TeamForm
from people.models import Participant
from django.core.mail import send_mail
from django.views import View
from hackworld.settings.base import EMAIL_HOST_USER
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


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
        if team.candidates.filter(user=participant.user):
            return JsonResponse({'success': False, 'message': f'Your request is already pending'})
        team.candidates.add(participant)
        res = send_mail(
            'Team join request',
            f'User {participant} wants to join your team {team.name}.',
            EMAIL_HOST_USER,
            [team.teamleader.user.email]
        )
        if res:
            return JsonResponse({'success': True, 'message': 'Mail sent'})
        return JsonResponse({'success': False, 'message': f'Added to candidates but could not send mail to {team.teamleader.user.email}'})


class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    template_name = 'teams/team-create.html'
    form_class = TeamForm

    def form_valid(self, form):
        print('valid')
        instance = form.save(commit=False)
        instance.teamleader = self.request.user.participant
        # participant = self.request.user.participant
        # data = self.request.POST.cleaned_data
        # team = Team(name=data.get('name'), teamleader=participant, looking_for=data.get('looking_for'),
        #             needed_skill=data.get('needed_skill'), description=data.get('description'))
        # team.save()
        instance.hackathon_id = self.request.GET.get('hackathon', 7)
        instance.save()
        instance.members.add(self.request.user.participant)
        instance.save()
        return redirect(reverse('people:profile'))
    def form_invalid(self, form):
        print(form.errors)


