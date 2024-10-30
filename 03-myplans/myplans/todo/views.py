from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from todo.models import Todo
from todo.serializers import TodoSerializer


# Create your views here.

class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()
