from django.urls import path
from .views import ParticipantCreate, LoginView, LogoutView, ProfileView, ParticipantCreateView, ParticipantUpdateView,\
                    Participantformset, DescriptionUpdateView, AlienProfileView, TeamListView

app_name = 'people'
urlpatterns = [
    path('register/', ParticipantCreate.as_view(), name='user-register'),
    path('skills/', Participantformset.as_view(), name='skills-edit'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('teams/', TeamListView.as_view(), name='teams-list'),
    path('', ProfileView.as_view(), name='profile'),
    path('update/', ParticipantUpdateView.as_view(), name='update'),
    path('description/', DescriptionUpdateView.as_view(), name='description'),
    path('<int:pk>/', AlienProfileView.as_view(), name='alien-profile'),
]
