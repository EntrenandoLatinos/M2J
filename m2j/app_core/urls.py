from django.urls import path
from app_core.views import general

app_name = 'app_core'
urlpatterns = [
    path('', general.index, name='index'),
    path('about/', general.about, name='about'),
    path('services/', general.services, name='services'),
    path('services/<int:pk>/', general.services_view, name='services_view'),
    path('faq/', general.faq, name='faq'),
    path('contact/', general.contact, name='contact'),
    path('privacy/', general.privacy, name='privacy'),
]