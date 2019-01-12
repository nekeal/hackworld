from django.db.models import Q
from django_filters import rest_framework as filters
from people.models import Skill, City

class SkillFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Skill
        fields = ('name',)


class CityFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name',method='name_filter')

    def name_filter(self, queryset, name, value):
        capitalized_value = value.capitalize()
        print(capitalized_value)
        return queryset.filter(Q(name__icontains=value) | Q(name__istartswith=capitalized_value))

    class Meta:
        model = City
        fields = ('name',)