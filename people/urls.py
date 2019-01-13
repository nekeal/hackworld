from django.urls import path
from .views import ParticipantCreate, LoginView, LogoutView, ProfileView, ParticipantCreateView, ParticipantUpdateView

app_name = 'people'
urlpatterns = [
    path('register/', ParticipantCreate.as_view(), name='user-register'),
    # path('test/', ParticipantUpdateView.as_view(), name='user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', ProfileView.as_view(), name='profile'),
    path('update/', ParticipantUpdateView.as_view(), name='profile'),
]
