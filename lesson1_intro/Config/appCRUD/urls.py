from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add_customer),
    path('list/', list_customer),
    path('delete/', customer_delete),
    path('update/', customer_update),
    path('search/', customer_search),
]