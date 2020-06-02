from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.clientslist, name='clients-list'),
    path('editar-cliente/<int:id>', views.clientedit, name="client-edit"),
    path('adicionar-cliente/', views.clientadd, name="client-add"),
    path('yourname/<str:name>', views.yourname, name='your-name'),
]