from django.urls import path
from .views import ParticipantCreate, LoginView, logout_view

urlpatterns = [
    path('register', ParticipantCreate.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='login'),
]
