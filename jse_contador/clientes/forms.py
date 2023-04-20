from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente

class NovoUsuarioForm(forms.ModelForm):
    cnpj = forms.CharField(max_length=14)
    email = forms.EmailField(required=True)
    razao_social = forms.CharField()
    nome_cliente = forms.CharField()
    telefone = forms.IntegerField()
    class Meta:
        model = Cliente
        fields = ['cnpj', 'email', 'razao_social', 'nome_cliente', 'telefone']