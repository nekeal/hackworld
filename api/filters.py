from django_filters import rest_framework as filters
from people.models import Skill

class SkillFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Skill
        fields = ('name',)