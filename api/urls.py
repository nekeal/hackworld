from django.urls import path, include
from .views import SkillsListApiView, CityListApiView



app_name = 'api'

urlpatterns = [
    path('skills/', SkillsListApiView.as_view(), name='skills'),
    path('cities/', CityListApiView.as_view(), name='cities'),
]
