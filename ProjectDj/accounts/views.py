import logging

from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from . import models
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from . import serializers
from django.contrib.auth import authenticate

# Create your views here.

logger = logging.getLogger('django')

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.AllowAny]



class AuthViewSet(viewsets.GenericViewSet):
    @action(detail=False, methods=['POST'])
    def register(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializers.UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'])
    def login(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['user']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user :
                refresh = RefreshToken.for_user(user)
                return Response({
                    'user': serializers.ProfileSerializer(user).data,
                    'access': str(refresh),
                    'refresh': str(refresh),
                })
            return Response({
                'error': 'Invalid credentials'
                }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'] , permission_classes=[permissions.IsAuthenticated])
    def logout(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            return Response({'message': 'Logged out successfully'})
        except:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['POST'] , permission_classes=[permissions.IsAuthenticated])
    def profile(self, request):
        serializer = serializers.ProfileSerializer(data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'] , permission_classes=[permissions.IsAuthenticated])
    def update_profile(self, request):
        serializer = serializers.ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)