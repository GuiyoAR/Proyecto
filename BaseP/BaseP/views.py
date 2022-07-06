from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from BaseP.forms import User_registration_form
from django.contrib.auth.decorators import login_required

# =============================================================
# INDEX PRINCIPAL
# =============================================================      
def index_view(request):
    context = {'message':f''}
    return render(request, 'index.html',context=context)

# =============================================================
# INDEX ADMINISTRACION
# =============================================================      
def index_admi(request):
    return render(request, 'administracion/indexadmin.html',context={})

# =============================================================
# INDEX ADMINISTRACION CLIENTES
# =============================================================      
def index_cli(request):
    return render(request, 'administracion/basecli.html',context={})

# =============================================================
# LOGUEO DE USUARIO
# =============================================================      
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    context = {'message':f'Administrador {username}'}
                    return render(request, 'administracion/indexadmin.html', context = context)
                else:
                    context = {'message':f'{username}'}
                    return render(request, 'clientes/indexcli.html', context = context)
            else:
                context = {'errors':'No hay ningun usuario con esas credenciales!!!'}
                form = AuthenticationForm()
                return render(request, 'clientes/indexcli.html', context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form} 
            return render(request, 'clientes/indexcli.html', context = context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'login.html', context = context)

# =============================================================
# REGISTRO DE USUARIO
# =============================================================      
def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message':f'{username}'}
            return render(request, 'index.html/', context = context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'register.html', context = context)
    else:
        form = User_registration_form()
        context = {'form':form}
        return render(request, 'register.html', context =context)

# =============================================================
# DESLOGUEO DE USUARIO
# =============================================================      
def logout_view(request):
    logout(request)
    return redirect('/')

# =============================================================
# Contacto VIEW
# =============================================================      
def contacto_view(request):
    return render(request, 'contacto.html', context={})

# =============================================================
# COMPRA VIEW
# =============================================================  
@login_required   
def compra_view(request):
    return render(request, 'compra.html',context={})