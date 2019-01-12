from rest_framework.serializers import ModelSerializer
from people.models import Skill, City

class SkillModelSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = ('name',)


class CityModelSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = ('name',)