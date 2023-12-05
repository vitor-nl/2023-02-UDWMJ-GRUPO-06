from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'orders'

urlpatterns = [
    path('', views.list_orderItens, name='list_orderItens'),
    path('adicionar/', views.add_orderItem, name='add_orderItem'),
    path('editar/<int:id_orderItem>/', views.edit_orderItem, name='edit_orderItem'),
    path('excluir/<int:id_orderItem>/', views.delete_orderItem, name='delete_orderItem'),
]