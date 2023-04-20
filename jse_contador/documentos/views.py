import os
from django.shortcuts import render
from django.template.context_processors import request
from clientes.models import Cliente
from .models import Documento
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

@login_required
def lista_documentos(request, id):
    """Lista todos os documentos disponíveis para o cliente"""
    documentos = Documento.objects.filter(cliente=id)

    dados = {
        'documentos': documentos,
    }
    return render(request, 'documentos.html', dados)

@login_required
def documentos(request):
    
    nome_documento = Documento.objects.order_by('id').filter(id)
    documentos_a_exibir = {
        'nome_documento': nome_documento
    }
    return(request)

@login_required
def download_arquivo(request, id):
    arquivo = Documento.objects.values_list('arquivo', flat=True).get(pk=id)
    result = os.path.join('./anexos/', arquivo)
    dados = {
        'dados': result
    }
    return FileResponse(open(result, 'rb'), content_type='application/pdf')

@login_required
def filtro_por_cliente(request):
    email_usuario = request.user.email
    cliente_logado = Cliente.objects.filter(email=email_usuario)
    id = cliente_logado.values('id')
    id_user = id[0]['id']
    todos_os_documentos = Documento.objects.all()
    documentos = todos_os_documentos.filter(cliente=id_user).order_by('-id')
    dados = {
        'documentos': documentos,
    }
    return render(request, 'documentos.html', dados)