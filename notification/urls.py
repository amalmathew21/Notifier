
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order_list/', views.order_list, name='order_list'),
    path('add_order/', views.add_order, name='add_order'),
    path('check_for_new_order/', views.check_for_new_order, name='check_for_new_order'),
]
