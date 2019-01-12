from django.urls import path
from .views import HackathonCreateView
app_name = 'hackathon'
urlpatterns = [
    path('create', HackathonCreateView.as_view(), name='create')
]
