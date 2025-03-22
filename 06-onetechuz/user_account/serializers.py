from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()

    class Meta(object):
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'gender', 'age', 'password', 'created_at')
        extra_kwargs = {'password': {'write_only': True}}


class LoginStartSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class LoginEndSerializer(serializers.ModelSerializer):
    code = serializers.CharField()
    code_token = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ('code', 'code_token')