from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic import ListView
from teams.models import Team
from .forms import UserRegisterForm, ParticipantForm
from .models import Participant, City, ParticipantSkill
from django.contrib.auth import views as auth_views
from .forms import ParticipantForm, ParticipantSkillFormset, UserUpdateForm, UserSimpleUpdateForm, DescriptionUpdateForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin




class TeamListView(ListView):
    template_name ='peoples/team_list.html'

    def get_queryset(self):
        qs = Team.objects.filter(Q(members__id=self.request.user.participant.id) | Q(teamleader=self.request.user.participant)).distinct()
        return qs

class DescriptionUpdateView(UpdateView):
    template_name = ''
    form_class = DescriptionUpdateForm
    success_url = '/profile/'

    def get_object(self, queryset=None):
        return self.request.user.participant
        #
        # def form_valid(self, form):
        #     print(form.cleaned_data)
        #     o = form.save(commit=False)
        #     o.description = form.cleaned_data['description']
        #     o.save()
        #     return HttpResponseRedirect('/profile/')

class ParticipantCreate(CreateView):
    form_class = UserRegisterForm
    template_name = 'peoples/registration.html'

    # template_name = 'tesst.html'

    def post(self, request):
        self.object = None
        user_form = UserRegisterForm(request.POST)
        city = City.objects.filter(name=request.POST['city']).first().id if City.objects.filter(
            name=request.POST['city']) else None
        # new_dict = {**request.POST, 'city':city.id}
        # print(new_dict['name'])
        skills_id = request.POST.get('skills')
        profile_form = ParticipantForm({"name": request.POST['name'], 'surname': request.POST['surname'], "city": city})
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            participant = profile_form.save(commit=False)
            participant.user = user
            participant.save()
            participant.refresh_from_db()
            for i in skills_id:
                ParticipantSkill.objects.create(skill_id=i, participant=participant)
        else:
            # print(self.object)
            return self.form_invalid(user_form)
            # participant.save()
        return HttpResponse('success')  # super(ParticipantCreate, self).post(request)

    # def form_valid(self, form):
    #     user = form.save()
    #     print('form valid')
    #     print(form.cleaned_data)
    #     part = Participant(name=form.cleaned_data.get('name'),
    #                        surname=form.cleaned_data.get('surname'),
    #                        city=City.objects.filter(name=form.cleaned_data.get('city'))
    #                        .first(),
    #                        user=user)
    #     part.save()
    #     return redirect('../admin/')

    # def form_invalid(self, form):
    #     print(form.errors)


class ParticipantCreateView(CreateView):
    form_class = ParticipantForm
    template_name = 'tesst.html'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return super(ParticipantCreateView, self).post(request, *args, **kwargs)


class LoginView(auth_views.LoginView):
    template_name = 'peoples/login.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        login(form.request, authenticate(form.request, username=form.cleaned_data.get('username'),
                                         password=form.cleaned_data.get('password')))
        return redirect(reverse('people:profile'))

    def form_invalid(self, form):
        return super().form_invalid(form)


class LogoutView(auth_views.LogoutView):
    next_page = '/'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'peoples/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        participant = Participant.objects.get(user=self.request.user)
        context['teams'] = participant.team_set.all()
        context['participant'] = participant
        # context['form'] = DescriptionUpdateForm()
        return context

class AlienProfileView(DetailView):
    template_name = 'peoples/alien_profile.html'
    queryset = Participant.objects.all()
    model = Participant
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     participant = Participant.objects.get(user=self.request.user)
    #     context['teams'] = participant.team_set.all()
    #     context['participant'] = participant
    #     # context['form'] = DescriptionUpdateForm()
    #     return context


class ParticipantUpdateView(FormView):
    form_class = UserUpdateForm
    template_name = 'peoples/edit-profile.html'
    queryset = Participant.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ParticipantUpdateView, self).get_context_data(**kwargs)
        context['form'] = self.get_form(self.form_class)
        return context

    def get_form(self, form_class=None):
        return self.form_class(
            initial={'name': self.request.user.participant.name,
                     'surname': self.request.user.participant.surname,
                     'city': self.request.user.participant.city,
                     'short_description': self.request.user.participant.short_description,
                     'email': self.request.user.email})
    #
    # def post(self, request):
    #     user_form = UserRegisterForm(request.POST)
    #     city = City.objects.filter(name=request.POST['city']).first().id if City.objects.filter(
    #         name=request.POST['city']) else None
    #     # new_dict = {**request.POST, 'city':city.id}
    #     # print(new_dict['name'])
    #     skills_id = request.POST.get('skills')
    #     profile_form = ParticipantForm({"name": request.POST['name'], 'surname': request.POST['surname'], "city": city})
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user = user_form.save()
    #         user.refresh_from_db()
    #         participant = profile_form.save(commit=False)
    #         participant.user = user
    #         participant.save()
    #         participant.refresh_from_db()
    #         for i in skills_id:
    #             ParticipantSkill.objects.create(skill_id=i, participant=participant)
    #     else:
    #         # print(self.object)
    #         return self.form_invalid(user_form)
    #         # participant.save()
    #     return HttpResponse('success')  # super(ParticipantCreate, self).post(request)

    def post(self, request):
        # user_form = UserSimpleUpdateForm(request.POST)
        city = City.objects.filter(name=request.POST['city']).first() if City.objects.filter(
            name=request.POST['city']) else None
        # new_dict = {**request.POST, 'city':city.id}
        # print(new_dict['name'])
        # skills_id = request.POST.get('skills')
        # profile_form = ParticipantForm({"name": request.POST['name'], 'surname': request.POST['surname'], "city": city}, instance=request.user.participant)
        # print(request.POST)
        profile_form = UserUpdateForm(request.POST)
        # print(user_form.is_valid(), profile_form.is_valid())
        print(profile_form.errors)
        if profile_form.is_valid():
            user = request.user
            profile_form.cleaned_data.update({'city': city.id})
            print(profile_form.cleaned_data)
            email = profile_form.cleaned_data.pop('email')
            user.email = email
            user.save()
            # user.refresh_from_db()
            # participant = profile_form.save(commit=True)

            participant = Participant.objects.filter(user=request.user).update(**profile_form.cleaned_data)
            # participant.user = user
            # participant.save()
            # participant.refresh_from_db()
            # for i in skills_id:
            #     ParticipantSkill.objects.create(skill_id=i, participant=participant)
        else:
            # print(self.object)
            return self.form_invalid(profile_form)
            # participant.save()
        return HttpResponseRedirect(reverse('people:profile'))  # super(ParticipantCreate, self).post(request)
    #
    # def get_object(self, queryset=None):
    #     return self.request.user# Participant.objects.get(user=self.request.user)
    #
    def form_valid(self, form):
        user = form.save()
        print('form valid')
        # print(form.cleaned_data)
        # part = Participant(name=form.cleaned_data.get('name'),
        #                    surname=form.cleaned_data.get('surname'),
        #                    city=City.objects.filter(name=form.cleaned_data.get('city'))
        #                    .first(),
        #                    user=user)
        # part.save()
        # return redirect('../admin/')
    # def form_invalid(self, form):
    #     print(form.errors)
    #     return HttpResponse('elo')

class Participantformset(UpdateView):
    model = Participant
    success_url='/profile/'
    template_name = 'tesst.html'
    form_class = ParticipantForm
    def get_context_data(self, **kwargs):
        context = super(Participantformset, self).get_context_data(**kwargs)
        if self.request.POST:
            context['skill_formset'] = ParticipantSkillFormset(self.request.POST, instance=self.object)
            context['skill_formset'].full_clean()
            print(context['skill_formset'].errors)
            print(context['form'].errors)
        else:
            context['skill_formset'] = ParticipantSkillFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['skill_formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))


    def get_object(self, queryset=None):
        return self.request.user.participant
        # return Participant.objects.get(user__username='admin')
