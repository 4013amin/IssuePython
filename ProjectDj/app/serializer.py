from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ('id', 'title', 'status', 'created_time', 'updated_time')