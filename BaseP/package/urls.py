from django.urls import path
from package import views
from package.views import list_ofertas, list_paquetes, busqueda_paquetes, vista_paquete, pkt_admin_view, lista_paquetes_adm, lista_paquetes_adm1, create_paquete_api_view, delete_paquetes, update_paquetes

urlpatterns =[
    # VISTAS DE PAQUETES EN LA PAGINA PRINCIPAL
    path('oferta-paquete/', list_ofertas, name = 'list_ofertas'),
    path('lista-paquete/', list_paquetes, name = 'list_paquetes'),
    path('vista-paquete/<int:pk>/', vista_paquete, name = 'vista_paquete'),
    # VISTAS DE PAQUETES PARA PARA PANEL ADMINISTRACION
    path('paquetes-main/', pkt_admin_view, name = 'pkt_admin_view'),
    path('alta-paquete/', create_paquete_api_view.as_view(), name = 'create_paquete_api_view'),
    path('lista-paquete-adm/', lista_paquetes_adm, name = 'lista_paquetes_adm'),
    path('baja-paquete/<int:pk>/', delete_paquetes, name = 'delete_paquetes'),
    path('lista-paquete-adm1/', lista_paquetes_adm1, name = 'lista_paquetes_adm1'),
    path('modificacion-paquete/<int:pk>/', update_paquetes.as_view(), name = 'update_paquetes'),
    path('busqueda-paquete/', busqueda_paquetes, name = 'busqueda_paquetes'),
]