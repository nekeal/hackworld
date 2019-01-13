from django.shortcuts import render, redirect, reverse
from django.views.generic.list import ListView
from django.http import JsonResponse
from .models import Team
from .forms import TeamForm, TeamUpdateForm
from people.models import Participant
from django.core.mail import send_mail
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views import View
from hackworld.settings.base import EMAIL_HOST_USER
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden, JsonResponse
import json
from django.db.models import Q



class AddDeleteCandidate(View):
    def post(self, request):
        data = json.loads(request.POST)
        team = Team.objects.get(id=data['team-id'])
        participant = Participant.objects.get(id=data['user-id'])
        if data['accept']:
            if team.members.count() >= team.hackathon.max_size:
                return {"success": False, 'message':'Maximum team size reached'}
            else:
                team.members.add(participant)
                team.candidates.remove(participant)
                return {"success": True, 'message': f'{participant.name} {participant.surname} added to team!'}
        else:
            team.candidates.remove(participant)
            return {"success": True, 'message': f'{participant.name} {participant.surname} removed from candidates!'}


class TeamListView(ListView):
    model = Team
    template_name = 'teams/team-list.html'


class TeamJoinRequestNotifier(View):
    def post(self, request):
        team_id = self.request.POST.get('team-id', self.request.GET.get('team-id'))
        try:
            team_id = int(team_id)
        except Exception:
            return JsonResponse({'success': False,
                                 'message': f'Invalid format POST={self.request.POST} GET={request.GET} method={request.method}'})
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
        return JsonResponse({'success': False,
                             'message': f'Added to candidates but could not send mail to {team.teamleader.user.email}'})


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


class TeamUpdateView(FormView):
    form_class = TeamUpdateForm
    template_name = 'peoples/edit-team.html'
    queryset = Participant.objects.all()
    success_url = '/profile/teams/'
    model = Team

    def dispatch(self, request, *args, **kwargs):
        id = kwargs['pk']
        team = get_object_or_404(Team, pk=id)
        if team.teamleader != request.user.participant:
            return HttpResponseForbidden()
        return super(TeamUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TeamUpdateView, self).get_context_data(**kwargs)
        context['form'] = self.get_form(self.form_class)
        id = self.kwargs['pk']
        context['members'] = Team.objects.get(pk=id)
        return context

    # def get_form(self, form_class=None):
    #     id = self.kwargs['pk']
    #     team = Team.objects.get(pk=id)
    #     form = self.form_class(
    #         initial={'description': team.description,
    #                  'looking_for': team.looking_for,
    #                  'needed_skill': team.needed_skill.all()
    #                  })
    #     return form
