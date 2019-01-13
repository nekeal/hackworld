from django.urls import path
from .views import TeamListView, TeamJoinRequestNotifier, TeamCreate, TeamUpdateView

urlpatterns = [
    path('list', TeamListView.as_view(), name='team-list'),
    path('join-request/', TeamJoinRequestNotifier.as_view(), name='profile'),
    path('create/', TeamCreate.as_view(), name='team-create'),
    path('update/<int:pk>', TeamUpdateView.as_view(), name='team-update'),
]
