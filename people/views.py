from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm
from .models import Participant, City
from django.contrib.auth import views as auth_views
from .forms import ParticipantForm
from django.contrib.auth import logout, login, authenticate


class ParticipantCreate(CreateView):
    form_class = UserRegisterForm
    template_name = 'peoples/registration.html'

    def form_valid(self, form):
        user = form.save()
        part = Participant(name=form.cleaned_data.get('name'),
                           surname=form.cleaned_data.get('surname'),
                           city=City.objects.get(name=form.cleaned_data.get('city')),
                           user=user)
        part.save()
        return redirect('../admin/')


class LoginView(auth_views.LoginView):
    template_name = 'user-login.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        login(form.request, authenticate(form.request, username=form.cleaned_data.get('username'),
                                         password=form.cleaned_data.get('password')))
        return redirect('/profile')

    def form_invalid(self, form):
        return super().form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect('/')



