                                   CODERHOUSE TRIP

Es una página web de una empresa de viajes. La página web tiene vistas de paquetes con destinos turísticos. El visitante puede navegar la página y ver los paquetes y ofertas de la empresa.

El presente código trabaja sobre la gestión de carga de 3 tablas principales (aunque no son las únicas).

Basicamente el sistema funciona con un visitante navegando la página. Cuando el visitante presiona el botón de compra de un PAQUETE el sistema pide registro/login del CLIENTE. Una vez logueado el sistema carga automaticamente una tabla de RESERVA con varios datos y también una tabla COMPRA (No implementada) donde se guardan los datos de compra y medio de pago.

-------------------------------------------
Tabla PAQUETE
-------------------------------------------
id                        (id del paquete - campo único)
destino                   (destino del viaje)
descripcion               (descripción del destino)
dias                      (días totales de viaje)
fecha_partida             (fecha de partida FORMATO: mm/dd/aaaa)
fecha_regreso             (fecha de regreso FORMATO: mm/dd/aaaa)
Image_Set_1               (nombre de la foto 1 del destino - carpeta MEDIA - No implementado)
Image_Set_2               (nombre de la foto 2 del destino - carpeta MEDIA - No implementado)
precio_publico            (Precio público del paquete)
costo                     (Costo del paquete) 
oferta                    (Indica si el paquete es una oferta)
activo                    (Indica si el paquete está activo)

-------------------------------------------
Tabla CLIENTE
-------------------------------------------
id                        (id del cliente - campo único)
nombre                    (Nombre del cliente)
apellido                  (Apellido del cliente)
pasaporte                 (Nro de pasaporte del cliente)
vencimiento               (Fecha de vencimiento del pasaporte)
dni                       (Nro de DNI del cliente)
domicilio                 (Domicilio del cliente)
telefono                  (Teléfono del cliente)
activo                    (Indica si cliente está activo)

-------------------------------------------
Tabla RESERVA
-------------------------------------------
id                        (id de reserva - campo único)
paquete                   (id de la tabla PAQUETE)
cliente                   (id de la tabla CLIENTE)
cantidad_pasajeros        (Cantidad de pasajeros que compró el paquete)
costo                     (Costo total de venta del paquete)
nro_factura               (Nro de factura si el paquete fue abonado)
estado                    (Estado del pago del paquete comprado. PG: pagado PE: pendiente de pago)
activo                    (Indica si la reserva está activa)

El código presentado trabaja sobre la administración de las tablas para ello tiene un menú con los siguientes items:

INICIO: Lleva al inicio de la GESTIÓN ADMINISTRATIVA DE CODERHOUSE TRIP

ALTA PAQUETE: Da de alta un paquete y se puede indicar si está en oferta o no.

ALTA CLIENTE: Da de alta un cliente. A futuro el cliente podrá registrarse en el sistema.

ALTA RESERVA: Da de alta una resevar. A futuro al comprar un paquete el sistema registrará el cliente y con los id de paquete e id de cliente se dará de alta la reserva 

BUSQUEDA: Busca paquete/s del destino introducido

#   C o d e r  
 