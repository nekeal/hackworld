from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.shortcuts import reverse
from .forms import UserRegisterForm, ParticipantForm
from .models import Participant, City, ParticipantSkill
from django.contrib.auth import views as auth_views
from .forms import ParticipantForm, ParticipantSkillFormset, UserUpdateForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


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
        return context


class ParticipantUpdateView(UpdateView):
    form_class = UserUpdateForm
    template_name = 'peoples/edit-profile.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ParticipantUpdateView, self).get_context_data(**kwargs)
    #     context['form'] = self.get_form(self.form_class)
    #     return context

    def get_form(self, form_class=None):
        return self.form_class(
            initial={'name': self.request.user.participant.name,
                     'surname': self.request.user.participant.surname,
                     'city': self.request.user.participant.city,
                     'short_description': self.request.user.participant.short_description,
                     'email': self.request.user.email})

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

    def get_object(self, queryset=None):
        return Participant.objects.get(user=self.request.user)

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


class Participantformset(UpdateView):
    model = Participant
    success_url='/profile/'
    template_name = 'tesst.html'
    form_class = ParticipantForm
    def get_context_data(self, **kwargs):
        context = super(ParticipantUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['skill_formset'] = ParticipantSkillFormset(self.request.POST, instance=self.object)
            context['skill_formset'].full_clean()
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
