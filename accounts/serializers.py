from rest_framework import serializers
from .models import User
from django.conf import settings



class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True , required = True)
    class Meta:
        model = User
        fields = ('email', 'username', 'password' , 'password2')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        del validated_data['password2']
        user = User.objects.create_user(**validated_data)
        return user


    def validate_username(self, value):
        if 'admin' in value:
            raise serializers.ValidationError('Username already taken')
        return value

    def validate(self , data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords do not match')
        return data


class UserShowSerializer(serializers.Serializer):
    email = serializers.EmailField(read_only=True)
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(read_only=True)
    is_admin = serializers.BooleanField(read_only=True)
    created  = serializers.DateTimeField(read_only=True)