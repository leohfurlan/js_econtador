from re import search
from django.contrib import admin
from .models import Documento

class ListandoDocumentos(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'nome_documento', 'arquivo')
    list_display_links = ('id', 'arquivo')
    search_fields = ('cliente', )
    list_per_page = 10

admin.site.register(Documento, ListandoDocumentos)