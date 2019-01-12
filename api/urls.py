from django.urls import path, include
from .views import SkillsListApiView



app_name = 'api'

urlpatterns = [
    path('skills/', SkillsListApiView.as_view(), name='skills'),
]
