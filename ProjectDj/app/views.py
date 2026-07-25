from django.shortcuts import render
from rest_framework import viewsets
from . import models
from .serializers import TaskSerializer


class TaskAPIView(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer
