from django.urls import path
from .views import ParticipantCreate, LoginView, LogoutView, ProfileView, ParticipantCreateView, ParticipantUpdateView,\
                    Participantformset

app_name = 'people'
urlpatterns = [
    path('register/', ParticipantCreate.as_view(), name='user-register'),
    path('skills/', Participantformset.as_view(), name='skills-edit'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', ProfileView.as_view(), name='profile'),
    path('update/', ParticipantUpdateView.as_view(), name='update'),
]
