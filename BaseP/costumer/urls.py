from django.urls import path
from costumer.views import create_clientes, cli_view, lista_clientes_baja, delete_clientes, cli_admin_view, lista_clientes_modif, update_clientes

urlpatterns =[
    # VISTAS DE LOGIN/REGISTRO PARA CLIENTES PAGINA
    path('cliente/', cli_view, name = 'cli_view'),
    # VISTAS DE CLIENTES PARA PARA PANEL ADMINISTRACION
    path('clientes-main/', cli_admin_view, name = 'cli_admin_view'),
    path('alta-cliente/', create_clientes, name = 'create_clientes'),
    path('lista-cliente-baja/', lista_clientes_baja, name = 'lista_clientes_baja'),
    path('lista-cliente-modif/', lista_clientes_modif, name = 'lista_clientes_modif'),
    path('baja-cliente/<int:pk>/', delete_clientes, name = 'delete_clientes'),
    path('modificacion-cliente/<int:pk>/', update_clientes.as_view(), name = 'update_clientes'),
]