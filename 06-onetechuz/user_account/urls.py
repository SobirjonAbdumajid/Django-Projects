from django.urls import path
from .views import RegisterApiView, LoginStartView, LoginEndView, FacebookLogin, FacebookData

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login_start/', LoginStartView.as_view()),
    path('login_end/', LoginEndView.as_view()),
    path('facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('facebook/data/', FacebookData.as_view(), name='fb_data'),
]