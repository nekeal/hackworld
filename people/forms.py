from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Participant, City, Skill, ParticipantSkill
from django.forms import ModelForm, Form
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

    # def clean_short_description(self):
    #     short_description = self.cleaned_data['short_description']
    #     return short_description or self.instance.participant.short_description
    #
    # def clean_description(self):
    #     description = self.cleaned_data['description']
    #     return description or self.instance.participant.description


# class UserUpdateForm(UserRegisterForm):
#     # def __init__(self,user, *args, **kwargs):
#     #     print(kwargs, user)
#     #     form = super(UserUpdateForm, self).__init__(*args, **kwargs)
#     #     # user = kwargs['user']
#     #     print(type(user))
#     #     self.initial['name'] = user.participant.name
#     #     return form
#     class Meta:
#         model = User
#         fields = ['email']

class UserUpdateForm(Form):
    city = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    name = forms.CharField(required=False)
    surname = forms.CharField(required=False)
    short_description = forms.CharField(required=False)

class ParticipantForm(ModelForm):
    # skills = forms.MultipleChoiceField(choices=ParticipantSkill.objects.values_list('id', flat=True))
    class Meta:
        model = Participant
        fields = ['name', 'surname', 'city', 'description']


    def clean_name(self):
        name = self.cleaned_data['name']
        return name or self.instance.name

    def clean_surname(self):
        surname = self.cleaned_data['surname']
        return surname or self.instance.surname

    def clean_city(self):
        city = self.cleaned_data['city']
        return city.id or self.instance.city_id

    def clean_description(self):
        description = self.cleaned_data['description']
        return description or self.instance.description


ParticipantSkillFormset = inlineformset_factory(Participant, ParticipantSkill, fields=['skill', 'advanced_level'],
                                                can_delete=True, extra=3)
