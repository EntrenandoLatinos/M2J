from django.contrib import admin
from app_core.models import Service, SubService, ServiceImage

# Register your models here.

admin.site.register(Service)
admin.site.register(SubService)
admin.site.register(ServiceImage)