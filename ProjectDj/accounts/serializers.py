from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . import  models

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        exclude = ['user']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=4, max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6, max_length=20, write_only=True)
    password_confirm = serializers.CharField(min_length=6, max_length=20, write_only=True)
    phone = serializers.CharField(min_length=11, max_length=11)
    full_name = serializers.CharField(max_length=100)
    address = serializers.CharField(required=False, allow_blank=True)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({
                "password": "Passwords do not match"
            })
        return data

    def create(self, validated_data):
        phone = validated_data.pop('phone')
        full_name = validated_data.pop('full_name')
        address = validated_data.pop('address', '')
        validated_data.pop('password_confirm')

        user = User.objects.create_user(**validated_data)

        models.Profile.objects.create(
            user=user,
            phone=phone,
            full_name=full_name,
            address=address
        )

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
