from django.db import models

# Create your models here.
class AuditoriaFecha(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Service(AuditoriaFecha):
    imagen = models.ImageField(upload_to='service/', null=True, blank=True)
    title = models.CharField("Service Name", max_length=60, null=True, blank=True)
    descripcion = models.TextField("Description", null=True, blank=True)
    descripcion_finish = models.TextField("Finish Description", null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return "{0}".format(str(self.title))
    
class SubService(AuditoriaFecha):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_subservice')
    imagen = models.ImageField(upload_to='service/', null=True, blank=True)
    title = models.CharField("Service Name", max_length=60, null=True, blank=True)
    descripcion = models.TextField("Description", null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'SubService'
        verbose_name_plural = 'SubServices'

    def __str__(self):
        return "{0}".format(str(self.title))
    
class ServiceImage(AuditoriaFecha):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_serviceimage')
    imagen = models.ImageField(upload_to='service_imagenes/')

    class Meta:
        ordering = ['id']
        verbose_name = 'ServiceImage'
        verbose_name_plural = 'ServiceImages'

    def __str__(self):
        return "{0}".format(str(self.service.nombre))
    