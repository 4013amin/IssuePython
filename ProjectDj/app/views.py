from django.shortcuts import render
from rest_framework import viewsets
from . import models
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer

class TaskAPIView(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()


from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)