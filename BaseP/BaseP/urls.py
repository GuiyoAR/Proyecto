
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from BaseP.views import index_view, login_view, logout_view, register_view, index_cli, index_admi, compra_view, contacto_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name = 'index_view'),
    path('cliente/', index_cli, name = 'index_cli'),
    path('administrador/', index_admi, name = 'index_admi'),
    path('compra/', compra_view, name = 'compra_view'),
    path('contacto/', contacto_view, name = 'contacto_view'),
    # VISTAS DE LOGIN REGISTRO Y LOGOUT
    path('login/', login_view, name = 'login_view'),
    path('register/', register_view, name = 'register_view'),
    path('logout/', logout_view, name = 'logout_view'),
    # URLS DE APPS
    path('paquetes/', include('package.urls')),
    path('clientes/', include('costumer.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
