from rest_framework.serializers import ModelSerializer
from people.models import Skill, City

class SkillModelSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = ('id','name',)


class CityModelSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = ('id','name',)