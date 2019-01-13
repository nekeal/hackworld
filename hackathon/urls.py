from django.urls import path
from .views import HackathonCreateView, HackathonDetailView

app_name = 'hackathon'

urlpatterns = [
    path('create', HackathonCreateView.as_view(), name='create'),
    path('<int:id>', HackathonDetailView.as_view(), name='detail'),
]
