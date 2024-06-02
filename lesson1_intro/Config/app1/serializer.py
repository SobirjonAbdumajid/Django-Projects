from rest_framework import serializers
from .models import Maqola

class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maqola
        fields = '__all__'