from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', LoginStart.as_view(), name='login'),
    path('loginend/', LoginEnd.as_view(), name='loginend'),
]
