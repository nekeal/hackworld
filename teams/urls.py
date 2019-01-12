from django.urls import path
from .views import TeamListView

urlpatterns = [
    path('list', TeamListView.as_view(), name='team-list'),
]
