from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm
from .models import Participant


class ParticipantCreate(CreateView):
    form_class = UserRegisterForm
    template_name = 'user-register.html'

    def form_valid(self, form):
        user = form.save()
        part = Participant(name=form.cleaned_data.get('name'),
                           surname=form.cleaned_data.get('surname'),
                           city=form.cleaned_data.get('city'),
                           user=user)
        part.save()
        return redirect('../admin/')
