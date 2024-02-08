from django.db import models
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import os

# Opciones para el campo de selección
CATEGORY_CHOICES = [
    ('01', 'Roofing'),
    ('02', 'Flat Roofing'),
    ('04', 'Siding'),
    ('05', 'Gutter'),
    ('06', 'Window'),
    ('07', 'Carpentry'),
    ('08', 'Remodeling'),
]

# Create your models here.
class AuditoriaFecha(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Contact(AuditoriaFecha):
    location = models.CharField("Location", max_length=100, null=True, blank=True)
    phone1 = models.CharField("Phone 2", max_length=60, null=True, blank=True)
    phone2 = models.CharField("Phone 1", max_length=60, null=True, blank=True)
    email = models.EmailField("Email", null=True, blank=True)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return "{0}".format(str(self.email))

class Banner(AuditoriaFecha):
    image = models.ImageField(upload_to='banner/', null=True, blank=True)
    title = models.CharField("Banner title", max_length=30, null=True, blank=True)
    subtitle = models.CharField("Banner subtitle", max_length=30, null=True, blank=True)
    description = models.TextField("Description", max_length=73, null=True, blank=True)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return "{0}".format(str(self.title))
    
class About(AuditoriaFecha):
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    about = models.TextField("About", null=True, blank=True)
    mision = models.TextField("Mision", null=True, blank=True)
    vision = models.TextField("Vision", null=True, blank=True)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return "{0}".format(str(self.id))
    
class Skill(AuditoriaFecha):
    title1 = models.CharField("Skill title 1", max_length=60, null=True, blank=True)
    description1 = models.TextField("Description 1", null=True, blank=True)
    title2 = models.CharField("Skill title 2", max_length=60, null=True, blank=True)
    description2 = models.TextField("Description 2", null=True, blank=True)
    title3 = models.CharField("Skill title 3", max_length=60, null=True, blank=True)
    description3 = models.TextField("Description 3", null=True, blank=True)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return "{0}".format(str(self.title1))
    
class Counter(AuditoriaFecha):
    title1 = models.CharField("Title 1", max_length=60, null=True, blank=True)
    number1 = models.IntegerField("Number 1", null=True, blank=True)
    title2 = models.CharField("Title 2", max_length=60, null=True, blank=True)
    number2 = models.IntegerField("Number 2", null=True, blank=True)
    title3 = models.CharField("Title 3", max_length=60, null=True, blank=True)
    number3 = models.IntegerField("Number 3", null=True, blank=True)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Counter'
        verbose_name_plural = 'Counters'

    def __str__(self):
        return "{0}".format(str(self.title1))

class Service(AuditoriaFecha):
    image = models.ImageField(upload_to='service/', null=True, blank=True)
    title = models.CharField("Service Name", max_length=60, null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    description_finish = models.TextField("Finish Description", null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return "{0}".format(str(self.title))
    
class SubService(AuditoriaFecha):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_subservice')
    image = models.ImageField(upload_to='subservice/', null=True, blank=True)
    title = models.CharField("Subservice Name", max_length=60, null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'SubService'
        verbose_name_plural = 'SubServices'

    def __str__(self):
        return "{0}".format(str(self.title))
    
class WorkImage(AuditoriaFecha):
    category = models.CharField("Category", null=True, blank=True, max_length=2, choices=CATEGORY_CHOICES)
    title = models.CharField("Image title", max_length=60, null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    image = models.ImageField(upload_to='work_image/')

    def __str__(self):
        return "{0}".format(str(self.title))
    
    def save(self, *args, **kwargs):
        if not self._state.adding:
            super().save(*args, **kwargs)
            return
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        img.save(self.image.path, quality=50)
                 
    class Meta:
        ordering = ['id']
        verbose_name = 'WorkImage'
        verbose_name_plural = 'WorkImages'

@receiver(pre_delete, sender=WorkImage)
def delete_gallery_image(sender, instance, **kwargs):
    file_path = instance.image.path
    if os.path.exists(file_path):
        os.remove(file_path)
    
class Testimonial(AuditoriaFecha):
    image = models.ImageField(upload_to='testimonial/', null=True, blank=True)
    name = models.CharField("Name", max_length=60, null=True, blank=True)
    location = models.CharField("Location", max_length=60, null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return "{0}".format(str(self.name))
    
class Partner(AuditoriaFecha):
    image = models.ImageField(upload_to='partner/', null=True, blank=True)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

    def __str__(self):
        return "{0}".format(str(self.id))
    
class Faq(AuditoriaFecha):
    title = models.CharField("Title", max_length=60, null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'

    def __str__(self):
        return "{0}".format(str(self.title))
    
class Privacy(AuditoriaFecha):
    title = models.CharField("Title", max_length=60, null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Privacy'
        verbose_name_plural = 'Privacies'

    def __str__(self):
        return "{0}".format(str(self.title))