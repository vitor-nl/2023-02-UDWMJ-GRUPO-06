from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'clients'

router = routers.DefaultRouter()
router.register('clientes', views.ClientViewSet, basename='clientes')
router.register('clientes_redessociais', views.ClientSocialnetworkViewSet, basename='clientes_redessociais')

urlpatterns = [
    path('', views.list_client, name='list_client'),
    path('adicionar/', views.add_client, name='add_client'),
    path('editar/<int:id_client>/', views.edit_client, name='edit_client'),
    path('excluir/<int:id_client>/', views.delete_client, name='delete_client'),

]