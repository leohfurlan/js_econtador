from re import search
from django.contrib import admin
from .models import Cliente

class ListandoClientes(admin.ModelAdmin):
    list_display = ('id', 'cnpj', 'razao_social', 'nome_cliente', 'telefone', 'email')
    list_display_links = ('id', 'cnpj','razao_social')
    search_fields = ('razao_social', )
    list_per_page = 10

admin.site.register(Cliente, ListandoClientes)