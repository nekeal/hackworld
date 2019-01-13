from .models import Team
from django import forms
from .models import Team, Participant, Skill


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'needed_skill', 'looking_for', 'description', 'hackathon']


class TeamUpdateForm(forms.ModelForm):
    description = forms.Textarea()
    looking_for = forms.BooleanField()
    needed_skill = forms.ModelMultipleChoiceField(Skill.objects.all())

    class Meta:
        model = Team
        fields = ['looking_for', 'description', 'needed_skill']
