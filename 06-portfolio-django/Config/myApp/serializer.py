from rest_framework import serializers
from .models import MaqolaModel

class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaqolaModel
        fields = '__all__'