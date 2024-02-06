from django.urls import path
from app_user.views import administrator

app_name = 'app_user'

urlpatterns = [
    path(
        'login/redirect/',
        administrator.login_redirect,
        name='login-redirect'
    ),
    path(
        'administrator/index/',
        administrator.admin_index,
        name='admin_index'
    ),
    path(
        'administrator/contact_update/',
        administrator.contact_update,
        name='contact_update'
    ),
    path(
        'administrator/banner_update/',
        administrator.banner_update,
        name='banner_update'
    ),
    path(
        'administrator/about_update/',
        administrator.about_update,
        name='about_update'
    ),
    path(
        'administrator/skill_update/',
        administrator.skill_update,
        name='skill_update'
    ),
    path(
        'administrator/counter_update/',
        administrator.counter_update,
        name='counter_update'
    ),
    path(
        'administrator/services/',
        administrator.services,
        name='services'
    ),
    path(
        'administrator/service_create/',
        administrator.service_create,
        name='service_create'
    ),
    path(
        'administrator/service_update/<int:pk>/',
        administrator.service_update,
        name='service_update'
    ),
    path(
        'administrator/subservices/<int:pk>/',
        administrator.subservices,
        name='subservices'
    ),
    path(
        'administrator/subservice_create/<int:pk>/',
        administrator.subservice_create,
        name='subservice_create'
    ),
    path(
        'administrator/subservice_update/<int:pk>/',
        administrator.subservice_update,
        name='subservice_update'
    ),
    path(
        'administrator/testimonials/',
        administrator.testimonials,
        name='testimonials'
    ),
    path(
        'administrator/testimonials_create/',
        administrator.testimonials_create,
        name='testimonials_create'
    ),
    path(
        'administrator/testimonial_update/<int:pk>/',
        administrator.testimonial_update,
        name='testimonial_update'
    ),
    path(
        'administrator/partners/',
        administrator.partners,
        name='partners'
    ),
    path(
        'administrator/partner_create/',
        administrator.partner_create,
        name='partner_create'
    ),
    path(
        'administrator/partner_update/<int:pk>/',
        administrator.partner_update,
        name='partner_update'
    ),
    path(
        'administrator/faqs/',
        administrator.faqs,
        name='faqs'
    ),
    path(
        'administrator/faq_create/',
        administrator.faq_create,
        name='faq_create'
    ),
    path(
        'administrator/faq_update/<int:pk>/',
        administrator.faq_update,
        name='faq_update'
    ),
    path(
        'administrator/privacy_update/',
        administrator.privacy_update,
        name='privacy_update'
    ),
]