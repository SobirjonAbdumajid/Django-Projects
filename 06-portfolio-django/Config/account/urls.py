from django.urls import path
from .views import *

urlpatterns = [
        path('login/', log_in, name='login'),
        path('register/', register, name='register'),
        path('logout/', log_out, name='logout'),
        path('confirmation/', code_confirmation, name='code_confirmation'),
        path('forget_password/', forget_password, name='forget_password'),
]