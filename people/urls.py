from django.urls import path
from .views import ParticipantCreate


urlpatterns = [
    path('register', ParticipantCreate.as_view(), name='user-register'),
]
