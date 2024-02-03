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
]