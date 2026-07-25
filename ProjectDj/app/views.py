from django.shortcuts import render
from rest_framework import viewsets
from . import models
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer