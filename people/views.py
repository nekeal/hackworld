from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .forms import UserRegisterForm, ParticipantForm
from .models import Participant, City, ParticipantSkill
from django.contrib.auth import views as auth_views
from .forms import ParticipantForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


class ParticipantCreate(CreateView):
    form_class = UserRegisterForm
    template_name = 'peoples/registration.html'

    # template_name = 'tesst.html'
    
    def post(self, request):
        user_form = UserRegisterForm(request.POST)
        city = City.objects.filter(name=request.POST['city']).first()
        new_dict = {**request.POST, 'city':city.id}
        skills_id = new_dict.get('skills')
        profile_form = ParticipantForm(new_dict)
        print(request.POST)
        print(user_form.is_valid(), profile_form.is_valid())
        print(profile_form.errors)
        print(user_form.errors)
        # print(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            self.object = user
            participant = profile_form.save(commit=False)
            participant.save()
            participant.refresh_from_db()
            participant.user = user
            for i in skills_id:
                ParticipantSkill.objects.create(skill_id=i, participant=participant)
        else:
            print(self.object)
            return self.form_invalid(user_form)
            # participant.save()
        return HttpResponse('success') # super(ParticipantCreate, self).post(request)
        
    def form_valid(self, form):
        user = form.save()
        print('form valid')
        print(form.cleaned_data)
        part = Participant(name=form.cleaned_data.get('name'),
                           surname=form.cleaned_data.get('surname'),
                           city=City.objects.filter(name=form.cleaned_data.get('city'))
                           .first(),
                           user=user)
        part.save()
        return redirect('../admin/')

    # def form_invalid(self, form):
    #     print(form.errors)

class ParticipantCreateView(CreateView):
    form_class = ParticipantForm
    template_name = 'tesst.html'


class LoginView(auth_views.LoginView):
    template_name = 'peoples/login.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        login(form.request, authenticate(form.request, username=form.cleaned_data.get('username'),
                                         password=form.cleaned_data.get('password')))
        return redirect('/profile/userprofile')

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
        return context
