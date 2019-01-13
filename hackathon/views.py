from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Hackathon
from teams.models import Team
from people.models import Participant
from .forms import HackathonForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.db.models import Count, Q
from django.contrib.auth.mixins import LoginRequiredMixin


class HackathonCreateView(LoginRequiredMixin, CreateView):
    model = Hackathon
    form_class = HackathonForm
    template_name = 'hackathon/hackathon-create.html'

    # success_url = '/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        message = f'Succesfully added hackathon "{instance.name}", now wait for admin confirmation'
        return render(self.request, 'hackathon/hackathon_create_success.html', context={'message': message})


class MainPage(ListView):
    template_name = 'hackathon/main-page.html'
    context_object_name = 'hackathons'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)

        comp = 0
        context['counts'] = {1: 12, 2: 123}
        context['incomplete_count'] = 0
        context['complete_count'] = 0
        context['res'] = self.get_queryset()
        return context

    def get_queryset(self):
        res = list(
            Hackathon.objects.filter(accepted=True).values('id', 'name', 'official_website', 'place_url', 'place',
                                                           'description', 'max_size', 'facebook_page', 'image', 'date'))
        for hack in res:
            hack['complete_c'] = 0
            hack['incomplete_c'] = 0
            for team in Team.objects.filter(hackathon__id=hack['id']):
                if team.members.count() >= hack['max_size']:
                    hack['complete_c'] += 1
                else:
                    hack['incomplete_c'] += 1
        return res


class HackathonDetailView(LoginRequiredMixin, ListView):
    # model = Team
    template_name = 'hackathon/hackathon_team_list.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(HackathonDetailView, self).get_context_data(**kwargs)
        context['hackathon'] = Hackathon.objects.get(id=self.kwargs['id'])
        context['queryset']  = self.get_queryset()
        if Team.objects.filter(hackathon__id=self.kwargs['id']).filter(Q(members=self.request.user.participant)| Q(teamleader=self.request.user.participant)).exists():
            context['has_team'] = True
            context['my_skills'] = list(self.request.user.participant.participantskill_set.values_list('skill__id',flat=True))
            print(context['my_skills'])
            context['my_team'] = Team.objects.filter(hackathon__id=self.kwargs['id']).filter(Q(members=self.request.user.participant) | Q(teamleader=self.request.user.participant)).distinct()
            context['queryset'] = self.get_queryset().exclude(name=Team.objects.filter(hackathon__id=self.kwargs['id']).filter(Q(members=self.request.user.participant) | Q(teamleader=self.request.user.participant)).distinct().first().name)
        return context

    def get_queryset(self):
        return Team.objects.filter(hackathon__id=self.kwargs['id'], looking_for=True)
