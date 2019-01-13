from .models import Team
from django import forms
from .models import Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'needed_skill', 'looking_for', 'description', 'hackathon']
