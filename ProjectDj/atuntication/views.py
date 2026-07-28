from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


from . import models
from . import serializers

# Create your views here.
class ProjectDashboard(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request,format=None):
        projects = models.Project.objects.all()
        serializer = serializers.ProjectSerializer(projects,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = serializers.ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        projects = models.Project.objects.get(id=pk)
        serializer = serializers.ProjectSerializer(instance=projects,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            profile = models.Project.objects.get(id=pk)
            profile.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)