from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Participant, City, Skill, ParticipantSkill
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.forms.widgets import TextInput


class UserRegisterForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    city = forms.ChoiceField(choices=((x, x) for x in City.objects.values_list('name', flat=True)), widget=TextInput,
                             required=True)
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), required=False)
    short_description = forms.CharField(max_length=100, required=False)
    description = forms.CharField(widget=TextInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_short_description(self, value):
        return value or self.instance.short_description

    def clean_description(self, value):
        return value or self.instance.description


class UserUpdateForm(UserRegisterForm):
    # def __init__(self,user, *args, **kwargs):
    #     print(kwargs, user)
    #     form = super(UserUpdateForm, self).__init__(*args, **kwargs)
    #     # user = kwargs['user']
    #     print(type(user))
    #     self.initial['name'] = user.participant.name
    #     return form
    class Meta:
        model = User
        fields = ['email']


class ParticipantForm(ModelForm):
    # skills = forms.MultipleChoiceField(choices=ParticipantSkill.objects.values_list('id', flat=True))
    class Meta:
        model = Participant
        fields = ['name',]# 'surname', 'city', 'description']


    def clean_name(self, value):
        return value or self.instance.name

    def clean_surname(self, value):
        return value or self.instance.surname

    def clean_city(self):
        return 0 or self.instance.city_id

    def clean_description(self, value):
        return value or self.instance.description


ParticipantSkillFormset = inlineformset_factory(Participant, ParticipantSkill, fields=['skill', 'advanced_level'],
                                                can_delete=True, extra=3)
