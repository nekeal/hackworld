from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Participant, City, Skill
from django.forms import ModelForm
from django.forms.widgets import TextInput

class UserRegisterForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    city = forms.CharField(widget=TextInput)
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'surname', 'city', 'skills']
