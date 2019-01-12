from rest_framework.serializers import ModelSerializer
from people.models import Skill


class SkillModelSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = ('name',)