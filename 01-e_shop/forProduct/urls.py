from django.urls import path
from .views import *

urlpatterns = [
    path('crud/', ProductApiView.as_view()),
    path('crud/<int:pk>/', ProductApiView.as_view()),
    path('category/', AddCategory.as_view()),
]
