from django.contrib import admin
from app_core.models import Service, ServiceImage

# Register your models here.

admin.site.register(Service)
admin.site.register(ServiceImage)