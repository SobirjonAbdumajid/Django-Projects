from django.urls import path
from .views import *

urlpatterns = [
    path('orders/', Add.as_view(), name='create-order'),
    path('add_order/', OrderAPIView.as_view(), name='create-order'),
    path('details/', OrderDetailAPIView.as_view()),
    # path('orders/', CreateOrderAPIView.as_view(), name='create-order'),
]