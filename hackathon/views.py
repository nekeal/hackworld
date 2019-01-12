from django.shortcuts import render
from django.views.generic import CreateView
from .models import Hackathon
from .forms import HackathonForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HackathonCreateView(CreateView):
    model = Hackathon
    form_class = HackathonForm
    template_name = 'tesst.html'
    # success_url = '/'


    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        message = f'Succesfully added hackathon "{instance.name}", now wait for admin confirmation'
        return render(self.request, 'hackathon/hackathon_create_success.html', context={'message':message})