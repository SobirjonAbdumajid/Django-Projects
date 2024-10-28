from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from todo.serializers import TodoSerializer


# Create your views here.

class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer