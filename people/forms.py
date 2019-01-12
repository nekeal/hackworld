from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Participant, City, Skill
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    city = forms.ModelChoiceField(queryset=City.objects.all())
    skill = forms.ModelMultipleChoiceField(queryset=Skill.objects.all())
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'surname', 'city']
