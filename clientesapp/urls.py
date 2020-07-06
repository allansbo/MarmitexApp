from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('clientes/', views.clientslist, name='clients-list'),
    path('editar-cliente/<int:id>', views.clientedit, name="client-edit"),
    path('deletar-cliente/<int:id>', views.clientdelete, name="client-delete"),
    path('ver-cliente/<int:id>', views.clientview, name="client-view"),
    path('adicionar-cliente/', views.clientadd, name="client-add"),
    path('yourname/<str:name>', views.yourname, name='your-name'),
    path('caixa/', views.caixa, name='caixa'),
    path('', views.dashboard, name='dashboard'),
    path('produto/', views.produto, name='produto'),
    path('produto-adicionar/', views.produto_adicionar, name='produto-adicionar'),
    path('pedido/', views.pedido, name='pedido'),
    path('pedido-adicionar/', views.pedido_adicionar, name='pedido-adicionar'),
]