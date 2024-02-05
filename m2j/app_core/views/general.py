from django.shortcuts import render
from app_core.models import Banner, Service


def index(request):
  banner = Banner.objects.all().last()
  servicios = Service.objects.all()
  context = {'servicios':servicios, 'banner':banner}
  return render(request, 'app_core/pages/index.html', context)

def about(request):
  servicios = Service.objects.all()
  context = {'servicios':servicios}
  return render(request, 'app_core/pages/about.html', context)

def services(request):
  servicios = Service.objects.all()
  context = {'servicios':servicios}
  return render(request, 'app_core/pages/services.html', context)

def services_view(request, pk):
  servicios = Service.objects.all()
  servicio = Service.objects.get(pk=pk)
  context = {'servicio':servicio, 'servicios':servicios}
  return render(request, 'app_core/pages/service.html', context)

def faq(request):
  servicios = Service.objects.all()
  context = {'servicios':servicios}
  return render(request, 'app_core/pages/faq.html', context)

def contact(request):
  servicios = Service.objects.all()
  context = {'servicios':servicios}
  return render(request, 'app_core/pages/contact.html', context)

def privacy(request):
  servicios = Service.objects.all()
  context = {'servicios':servicios}
  return render(request, 'app_core/pages/privacy.html', context)
