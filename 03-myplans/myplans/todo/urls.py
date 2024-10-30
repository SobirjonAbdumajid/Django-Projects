from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import TodoViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('todo', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token)
]

