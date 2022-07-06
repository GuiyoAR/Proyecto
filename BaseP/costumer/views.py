from django.http import HttpResponse
from django.shortcuts import render

from costumer.forms import Cliente_form
from costumer.models import Cliente

from django.urls import reverse 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# =============================================================  
# VISTA DE LOGIN CLIENTES
# =============================================================  
def cli_view(request):
    return render(request, 'clientes/indexcli.html', context={})

    
# =====================================================================================================
# **************                           ZONA ADMINISTRACION                           ************** 
# ===================================================================================================== 

# =============================================================  
# VISTA DE CLIENTES EN ADMINISTRACION
# =============================================================  
def cli_admin_view(request):
    return render(request, 'clientes/clientes.html', context={})

# =============================================================  
# ALTA DE CLIENTES
# =============================================================  
def create_clientes(request):
    if request.method == 'GET':
        form = Cliente_form()
        context = {'form':form}
        return render(request, 'clientes/alta-cliente.html', context=context)
    elif request.method == 'POST':
        form = Cliente_form(request.POST)
        if form.is_valid():
            new_cliente = Cliente.objects.create(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                pasaporte = form.cleaned_data['pasaporte'],
                vencimiento = form.cleaned_data['vencimiento'],
                dni = form.cleaned_data['dni'],
                domicilio = form.cleaned_data['domicilio'],
                telefono = form.cleaned_data['telefono'],
                activo = form.cleaned_data['activo'],
            )
            context = {'new_cliente':new_cliente}
        else:
            context = {'errors':form.errors}
        return render(request, 'clientes/alta-cliente.html', context = context)

    else:
        return HttpResponse('Only GET and POST methods are allowed')

# =============================================================  
# LISTADO DE CLIENTES ACTIVOS PARA BAJA
# =============================================================   
def lista_clientes_baja(request):
    clientes1 = Cliente.objects.filter(activo=True)
    context = {'pkq':clientes1}
    return render(request, 'clientes/lista-cliente-baja.html', context=context)

# =============================================================  
# BAJA DE CLIENTES
# =============================================================  
def delete_clientes(request, pk):
    # try:
        if request.method == 'GET':
            deletecli = Cliente.objects.get(id=pk)
            context = {'dlt':deletecli}
            return render(request, 'clientes/baja-cliente.html', context=context)
        else:
            deletecli = Cliente.objects.get(id=pk)
            deletecli.delete()
            context = {'message':'Cliente eliminado correctamente'}
            return render(request, 'clientes/clientes.html', context=context)
        
# =============================================================  
# LISTADO DE CLIENTES ACTIVOS PARA MODIFICACION
# =============================================================   
def lista_clientes_modif(request):
    clientes1 = Cliente.objects.filter(activo=True)
    context = {'pkq':clientes1}
    return render(request, 'clientes/lista-cliente-modif.html', context=context)

# =============================================================  
# MODIFICACION CLIENTES
# =============================================================  
class update_clientes(UpdateView):
    model = Cliente 
    template_name = 'clientes/modificacion-cliente.html'
    fields = '__all__'
    
    def get_success_url(self):
        success_url = '/clientes/lista-cliente-modif/'
        return success_url

# =============================================================  
# BUSQUEDA DE CLIENTES
# =============================================================   
def busqueda_clientes(request):
    clientes = Cliente.objects.filter(apellido__icontains=request.GET['search'])
    if clientes.exists():
        context = {'cli':clientes}
    else:
        context = {'errors':'No se encontro el cliente'}
    return render(request, 'clientes/busqueda-cliente.html', context = context)
