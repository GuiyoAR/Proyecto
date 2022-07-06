# Coder
Este trabajo fue desarrollado integramente por mi. 

Es una página web para venta de paquetes turísticos. Esto consta de PAQUETES que son ofrecidos para la venta. Cuenta con una parte de CLIENTES que debe ser accedida para poder realizar la compra. 

Tiene 3 APPS que son:
- Costumer
- Package
- Users

Hay un breve video explicativo de la pag: https://youtu.be/kK_mrV-qe-8

App COSTUMER:

Tiene los clientes: 
- mlopez
- mperez
- gfernandez
- luca

El pass de todos ellos es: hola3215

Hay un usuario administrador:
user:  admin
pass: 123123

App PACKAGE

Se pueden cargar en el PANEL ADMINISTRADOR dos paquetes (RIO DE JANEIRO y ROMA) con cualquier dato. Los archivos de imágenes deben ser respetados por los tamaños  (ej. imagen 1 = rio1.jpg /... / imagen 4 = rio4,jPG). 
Enlace de los datos para cargar: https://drive.google.com/drive/folders/1xIGtvH0Khdcvv07ALQg2P7X7fBDzr_x1?usp=sharing

PANEL ADMINISTRADOR se puede modificar los datos de CLIENTES y PAQUETES (Alta, Baja, Modificación)

ERROR DETECTADO:
Se detectó un error en la parte de profile del usuario. El programa registra un nuevo usuario y cuando un usuario está logueado en el panel CLIENTES puede editar el PERFIL pero da un error. El problema es que la funcion no liga al USER de la BD con el USER_PROFILE declarado en la función users. Este mismo error se detectó en el ECOMMERCE que se hizo en clase (branck LAST_CLASS). Se puede creear un usuario pero al tratar de editarlo  (con un click sobre la imagen) aparece el error. 
Realmente se realizó una investigación y consultas sin encontrar el resultado. 
Estaría bueno, si es posible, alguna idea de cual es exactamente el problema y la solución del mismo. 

Muchas gracias!
GUILLERMO MARCELO FLORES

