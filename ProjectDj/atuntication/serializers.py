from rest_framework import serializers
from . import models

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'


class ActuationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'
