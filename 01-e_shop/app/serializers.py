from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class LoginStartSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

class LoginEndSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField()
    code_token = serializers.CharField()

