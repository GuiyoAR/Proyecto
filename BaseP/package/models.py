from django.db import models


class Paquete(models.Model):
    destino = models.CharField(max_length=40)    
    descripcion = models.CharField(max_length=200)   
    dias = models.IntegerField()
    fecha_partida = models.DateField()
    fecha_regreso = models.DateField()
    Image_Set_1 = models.ImageField(upload_to='pack_profile', default='default.jpg')
    Image_Set_2 = models.ImageField(upload_to='pack_profile', default='default.jpg')
    Image_Set_3 = models.ImageField(upload_to='pack_profile', default='default.jpg')
    Image_Set_4 = models.ImageField(upload_to='pack_profile', default='default.jpg')
    precio_publico = models.IntegerField()
    costo = models.FloatField()
    oferta = models.BooleanField()
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'paquete'
        verbose_name_plural = 'paquetes'

    def __str__(self):
        return self.destino