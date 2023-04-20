from django.urls import path
from . import views

urlpatterns = [
    path("", views.documentos, name="documentos"),
    path('lista_documentos/<int:id>', views.lista_documentos, name='lista_documentos'),
    path('lista_documentos/<int:id>/download', views.download_arquivo, name='download'),
    path('filtro_por_cliente/', views.filtro_por_cliente, name='filtro_por_cliente')
]