from django.urls import path

from . import views

urlpatterns = [
    path("", views.clientes, name="clientes"),
    path("cadastrar_cliente/", views.Cadastro.cadastrar_cliente, name="cadastrar_cliente"),
]