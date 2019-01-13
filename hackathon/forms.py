from django import forms
from .models import Hackathon


class HackathonForm(forms.ModelForm):
    class Meta:
        model = Hackathon
        fields = (
            'name', 'proof', 'official_website', 'facebook_page', 'date', 'image', 'place_url', 'place',
            'max_size')
