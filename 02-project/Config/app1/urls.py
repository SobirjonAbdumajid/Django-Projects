from django.urls import path
from .views import *

urlpatterns = [
    path('', maqola, name='maqola'),
    path('world/', worldNews, name='world'),
    path('sport/', sport, name='sport'),
    path('local/', local, name='local'),
    path('article_detail/<int:id>', article_detail, name='article_detail'),
    path('add/', add_customer),
    path('list/', list_customer),
    path('delete/', customer_delete),
    path('update/', customer_update),
    path('search/', customer_search),
]
