from django.shortcuts import render, redirect
from django.shortcuts import redirect, render  
from .forms import UserForm

def index(request):
    
    return redirect('/accounts/login')

  
def register(request):  
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm() 
    context = {  
        'form':form  
    }  
    return render(request, 'register_usuario.html', context)  