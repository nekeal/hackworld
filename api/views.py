

from rest_framework.generics import ListAPIView
from  django_filters.rest_framework import DjangoFilterBackend
from people.models import Skill, City
from .serializers import SkillModelSerializer, CityModelSerializer
from .filters import SkillFilter, CityFilter

class SkillsListApiView(ListAPIView):
    queryset = Skill.objects.all()
    filter_backends = (DjangoFilterBackend,)
    serializer_class = SkillModelSerializer
    filterset_class = SkillFilter

class CityListApiView(ListAPIView):
    queryset = City.objects.all()
    filter_backends = (DjangoFilterBackend,)
    serializer_class = CityModelSerializer
    filterset_class = CityFilter