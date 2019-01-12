from django.urls import path
from .views import TeamListView, TeamJoinRequestNotifier

urlpatterns = [
    path('list', TeamListView.as_view(), name='team-list'),
    path('join-request/', TeamJoinRequestNotifier.as_view(), name='profile'),
]
