from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from package.forms import Paquete_form
from package.models import Paquete

from django.views.generic import  CreateView, UpdateView

# =============================================================
# LISTADO DE OFERTAS
# =============================================================      
def list_ofertas(request):
    paquetes1 = Paquete.objects.filter(oferta=True)
    context = {'pkq':paquetes1}
    return render(request, 'paquetes/oferta-paquete.html', context=context)

# =============================================================  
# LISTADO DE PAQUETES
# =============================================================   
def list_paquetes(request):
    paquetes1 = Paquete.objects.filter(activo=True)
    context = {'pkq':paquetes1}
    return render(request, 'paquetes/lista-paquete.html', context=context)

# =============================================================
# VISTA DE UN PAQUETE
# =============================================================      
def vista_paquete(request, pk):
        paquete = Paquete.objects.get(id=pk)
        context = {'pkq':paquete}
        return render(request, 'paquetes/paquete-view.html', context=context)

# =====================================================================================================
# **************                           ZONA ADMINISTRACION                           ************** 
# ===================================================================================================== 

# =============================================================  
# VISTA DE PAQUETES EN PANEL ADMINISTRACION
# =============================================================  
def pkt_admin_view(request):
    return render(request, 'paquetes/paquetes.html', context={})

# =============================================================  
# ALTA DE PAQUETES
# =============================================================  
class create_paquete_api_view(CreateView):
    model = Paquete
    template_name = 'paquetes/alta-paquete.html'
    fields = '__all__'

    def get_success_url(self):
        success_url = '/paquetes/paquetes-main/'
        return success_url

# =============================================================  
# LISTADO DE PAQUETES ACTIVOS PARA BAJA
# =============================================================   
def lista_paquetes_adm(request):
    paquetes1 = Paquete.objects.filter(activo=True)
    context = {'pkq':paquetes1}
    return render(request, 'paquetes/lista-paquete-baja.html', context=context)

# =============================================================  
# BAJA DE PAQUETES
# =============================================================  
def delete_paquetes(request, pk):
    if request.method == 'GET':
        deletepkt = Paquete.objects.get(id=pk)
        context = {'dlt':deletepkt}
        return render(request, 'paquetes/baja-paquete.html', context=context)
    else:
        deletepkt = Paquete.objects.get(id=pk)
        deletepkt.delete()
        context = {'message':'Paquete eliminado correctamente'}
        return render(request, 'paquetes/paquetes.html', context=context)
        
# =============================================================  
# LISTADO DE PAQUETES ACTIVOS PARA MODIFICAR
# =============================================================   
def lista_paquetes_adm1(request):
    paquetes1 = Paquete.objects.filter(activo=True)
    context = {'pkq':paquetes1}
    return render(request, 'paquetes/lista-paquete-modif.html', context=context)

# =============================================================  
# MODIFICACION PAQUETES
# =============================================================  
class update_paquetes(UpdateView):
    model = Paquete 
    template_name = 'paquetes/modificacion-paquete.html'
    fields = '__all__'
    
    def get_success_url(self):
        success_url = '/paquetes/lista-paquete-adm1/'
        return success_url
    
# =============================================================  
# BUSQUEDA PAQUETES
# =============================================================     
def busqueda_paquetes(request):
    paquetes = Paquete.objects.filter(destino__icontains=request.GET['search'])
    if paquetes.exists():
        context = {'pkt':paquetes}
    else:
        context = {'errors':'No se encontro el paquete'}
    return render(request, 'paquetes/busqueda-paquete.html', context = context)