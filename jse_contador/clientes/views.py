from django.shortcuts import render, get_object_or_404
from .models import Cliente
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import View


@login_required
def clientes(request):
    """Lista todos os clientes cadastrados no sistema"""
    clientes = Cliente.objects.all
    dados = {'clientes': clientes}
    return render(request, 'clientes.html', dados)


class Cadastro(View):    
    def cadastrar_cliente(request):
        context = {}
        form = NovoUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        context['form']  = form

        return render(request, 'documentos.html', context)

    