

from rest_framework.generics import ListAPIView
from  django_filters.rest_framework import DjangoFilterBackend
from people.models import Skill
from .serializers import SkillModelSerializer
from .filters import SkillFilter

class SkillsListApiView(ListAPIView):
    queryset = Skill.objects.all()
    filter_backends = (DjangoFilterBackend,)
    serializer_class = SkillModelSerializer
    filterset_class = SkillFilter
    # filter_fields = ('name',)