from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('certificates/', certificates, name='certificates'),
    path('projects/', projects, name='projects'),
    path('education/', education, name='education'),
    path('article_details/<int:id>', article_details, name='article_details'),
    path('add/', add, name='add'),
    path('list/', list, name='list'),
    path('delete/', delete, name='delete'),
    path('update/', update, name='update'),
    path('search/', search, name='search')
]