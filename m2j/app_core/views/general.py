from django.shortcuts import render
from app_core.models import Contact, Banner, About, Skill, Counter, Service, SubService, WorkImage, Testimonial, Partner, Faq, Privacy, SocialMedia


def index(request):
  contact = Contact.objects.all().last()
  banner = Banner.objects.all().last()
  about = About.objects.all().last()
  skills = Skill.objects.all().last()
  indicators = Counter.objects.all().last()
  servicios = Service.objects.all()
  gallery = WorkImage.objects.all().order_by('?')[:6]
  testimonials = Testimonial.objects.all()
  partners = Partner.objects.all()
  social_media = SocialMedia.objects.all()
  context = {
    'contact':contact,
    'banner':banner,
    'about':about,
    'skills':skills,
    'indicators':indicators,
    'servicios':servicios,
    'gallery':gallery,
    'testimonials':testimonials,
    'partners':partners,
    'social_media':social_media,
    }
  return render(request, 'app_core/pages/index.html', context)

def about(request):
  about = About.objects.all().last()
  skills = Skill.objects.all().last()
  servicios = Service.objects.all()
  context = {'servicios':servicios, 'about':about, 'skills':skills,}
  return render(request, 'app_core/pages/about.html', context)

def services(request):
  servicios = Service.objects.all()
  context = {'servicios':servicios}
  return render(request, 'app_core/pages/services.html', context)

def services_view(request, pk):
  servicios = Service.objects.all()
  servicio = Service.objects.get(pk=pk)
  subservicios = SubService.objects.filter(service=pk)
  context = {'servicio':servicio, 'servicios':servicios, 'subservicios':subservicios}
  return render(request, 'app_core/pages/service.html', context)

def works(request):
  servicios = Service.objects.all()
  gallery = WorkImage.objects.all().order_by('?')
  context = {
    'servicios':servicios,
    'gallery':gallery,
  }
  return render(request, 'app_core/pages/works.html', context)

def faq(request):
  faqs = Faq.objects.all()
  servicios = Service.objects.all()
  context = {'servicios':servicios, 'faqs':faqs}
  return render(request, 'app_core/pages/faq.html', context)

def contact(request):
  contact = Contact.objects.all().last()
  servicios = Service.objects.all()
  testimonials = Testimonial.objects.all()
  context = {'servicios':servicios, 'contact':contact, 'testimonials':testimonials}
  return render(request, 'app_core/pages/contact.html', context)

def privacy(request):
  servicios = Service.objects.all()
  privacy = Privacy.objects.all().last()
  context = {'servicios':servicios, 'privacy':privacy}
  return render(request, 'app_core/pages/privacy.html', context)
