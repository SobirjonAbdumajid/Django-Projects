from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import TodoViewSet
from rest_framework.authtoken import views


router = DefaultRouter()
router.register('todo', TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token)
]

