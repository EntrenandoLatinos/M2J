from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def login_redirect(request):
    if request.user.is_superuser:
        return redirect('app_user:admin_index')
    
@login_required
def admin_index(request):
    context = {}
    return render(request, 'app_user/base.html', context)