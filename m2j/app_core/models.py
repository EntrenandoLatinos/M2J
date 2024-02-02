from django.db import models

# Create your models here.
class AuditoriaFecha(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Service(AuditoriaFecha):
    nombre = models.CharField("Nombre del servicio", max_length=60, default='', null=True, blank=True)
    descripcion = models.TextField("Descripción", null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return "{0}".format(str(self.nombre))
    
class ServiceImage(AuditoriaFecha):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/')

    class Meta:
        ordering = ['id']
        verbose_name = 'ServiceImage'
        verbose_name_plural = 'ServiceImages'

    def __str__(self):
        return "{0}".format(str(self.service.nombre))