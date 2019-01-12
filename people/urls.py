from django.urls import path
from .views import ParticipantCreate, LoginView, logout_view, ProfileView

app_name = 'people'
urlpatterns = [
    path('register', ParticipantCreate.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('userprofile/', ProfileView.as_view(), name='profile')
]
