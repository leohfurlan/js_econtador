from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from clientes.models import Cliente
from django.core.exceptions import ValidationError

clientes_choices = Cliente.objects.values_list('id', 'email')

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )



class Formulario_Cadastrar_Usuario(UserCreationForm):
    razao_social = forms.ChoiceField(choices=clientes_choices)
    usuario = forms.CharField()

    class Meta:
        model = User
        fields = ["razao_social", "usuario"]

    def usuario_clean(self):  
        username = self.cleaned_data['usuario'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("Usuário já existe")  
        return username

    def clean_password2(self):
        senha1 = self.cleaned_data['senha1']  
        senha2 = self.cleaned_data['senha2']  
        if senha1 and senha2 and senha1 != senha2:  
            raise ValidationError("Senhas não são iguais")  
        return senha2  

    def save(self, commit = True):
        user = User.objects.create_user(
            self.cleaned_data['usuario'],  
            self.cleaned_data['razao_social'],  
            self.cleaned_data['senha1']
        )
        return user

#class UserLogin(UserCreationForm):
