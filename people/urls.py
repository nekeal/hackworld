from django.urls import path
from .views import ParticipantCreate, LoginView, LogoutView, ProfileView, ParticipantCreateView

app_name = 'people'
urlpatterns = [
    path('register/', ParticipantCreate.as_view(), name='user-register'),
    path('test/', ParticipantCreateView.as_view(), name='user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', ProfileView.as_view(), name='profile'),
]
