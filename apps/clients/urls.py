from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'clients'


urlpatterns = [
    path('', views.list_client, name='list_clients'),
    path('adicionar/', views.add_client, name='add_client'),
    path('editar/<int:id_client>/', views.edit_client, name='edit_client'),
    path('clientes/excluir/<int:id_client>/', views.delete_clients, name='delete_clients'),

]