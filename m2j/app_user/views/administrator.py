from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from app_core.forms import ContactForm, BannerForm, AboutForm, SkillForm, CounterForm, ServiceForm, SubServiceForm, TestimonialForm, TestimonialDeleteForm, PartnerForm, FaqForm, PrivacyForm
from app_core.models import Contact, Banner, About, Skill, Counter, Service, SubService, Testimonial, Partner, Faq, Privacy

def login_redirect(request):
    if request.user.is_superuser:
        return redirect('app_user:admin_index')
    
@login_required
def admin_index(request):
    context = {}
    return render(request, 'app_user/base.html', context)

@login_required
def contact_update(request):
    contact = Contact.objects.all().last()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES, instance=contact)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('app_user:admin_index')
    else:
        contact_form = ContactForm(instance=contact)

    context = {'contact':contact, 'contact_form':contact_form}
    return render(request, 'app_user/pages/contact.html', context)

@login_required
def banner_update(request):
    banner = Banner.objects.all().last()

    if request.method == 'POST':
        banner_form = BannerForm(request.POST, request.FILES, instance=banner)
        if banner_form.is_valid():
            banner_form.save()
            return redirect('app_user:admin_index')
    else:
        banner_form = BannerForm(instance=banner)

    context = {'banner':banner, 'banner_form':banner_form}
    return render(request, 'app_user/pages/banner.html', context)

@login_required
def about_update(request):
    about = About.objects.all().last()

    if request.method == 'POST':
        about_form = AboutForm(request.POST, request.FILES, instance=about)
        if about_form.is_valid():
            about_form.save()
            return redirect('app_user:admin_index')
    else:
        about_form = AboutForm(instance=about)

    context = {'about':about, 'about_form':about_form}
    return render(request, 'app_user/pages/about.html', context)

@login_required
def skill_update(request):
    skill = Skill.objects.all().last()

    if request.method == 'POST':
        skill_form = SkillForm(request.POST, request.FILES, instance=skill)
        if skill_form.is_valid():
            skill_form.save()
            return redirect('app_user:admin_index')
    else:
        skill_form = SkillForm(instance=skill)

    context = {'skill':skill, 'skill_form':skill_form}
    return render(request, 'app_user/pages/skill.html', context)

@login_required
def counter_update(request):
    counter = Counter.objects.all().last()

    if request.method == 'POST':
        counter_form = CounterForm(request.POST, request.FILES, instance=counter)
        if counter_form.is_valid():
            counter_form.save()
            return redirect('app_user:admin_index')
    else:
        counter_form = CounterForm(instance=counter)

    context = {'counter':counter, 'counter_form':counter_form}
    return render(request, 'app_user/pages/counter.html', context)

@login_required
def services(request):
    services = Service.objects.all()
    context = {'services':services}
    return render(request, 'app_user/pages/services.html', context)

@login_required
def service_create(request):
    if request.method == 'POST':
        service_form = ServiceForm(request.POST, request.FILES)
        if service_form.is_valid():
            new_service = service_form.save()
            return redirect('app_user:services')
    else:
        service_form = ServiceForm()

    return render(request, 'app_user/pages/service_create.html', {'service_form': service_form})

@login_required
def service_update(request, pk):
    service = get_object_or_404(Service, id=pk)

    if request.method == 'POST':
        service_form = ServiceForm(request.POST, request.FILES, instance=service)
        if service_form.is_valid():
            service_form.save()
            return redirect('app_user:services')
    else:
        service_form = ServiceForm(instance=service)

    context = {'service':service, 'service_form':service_form}
    return render(request, 'app_user/pages/service_update.html', context)

@login_required
def testimonials(request):
    testimonials = Testimonial.objects.all()
    context = {'testimonials':testimonials}
    return render(request, 'app_user/pages/testimonials.html', context)

@login_required
def testimonials_create(request):
    if request.method == 'POST':
        testimonial_form = TestimonialForm(request.POST, request.FILES)
        if testimonial_form.is_valid():
            new_testimonial = testimonial_form.save()
            return redirect('app_user:testimonials')
    else:
        testimonial_form = TestimonialForm()

    return render(request, 'app_user/pages/testimonials_create.html', {'testimonial_form': testimonial_form})

@login_required
def testimonial_update(request, pk):
    testimonial = get_object_or_404(Testimonial, id=pk)

    if request.method == 'POST':
        if 'update_testimonial' in request.POST:
            testimonial_form = TestimonialForm(request.POST, request.FILES, instance=testimonial, prefix='testimonial_update')
            
            if testimonial_form.is_valid():
                testimonial_form.save()
                return redirect('app_user:testimonials')
        
        elif 'delete_testimonial' in request.POST:
            print("Paso 1")
            testimonial_delete_form = TestimonialDeleteForm(request.POST, prefix='testimonial_delete', initial={'id_to_delete': pk})
            if testimonial_delete_form.is_valid():
                print("Paso 2")
                id_to_delete = testimonial_delete_form.cleaned_data['id_to_delete']
                # Eliminar el registro con el id especificado
                Testimonial.objects.filter(id=id_to_delete).delete()
                return redirect('app_user:testimonials')
    else:
        testimonial_form = TestimonialForm(instance=testimonial, prefix='testimonial_update')
        testimonial_delete_form = TestimonialDeleteForm(prefix='testimonial_delete', initial={'id_to_delete': pk})

    context = {'testimonial':testimonial, 'testimonial_form':testimonial_form, 'testimonial_delete_form':testimonial_delete_form}
    return render(request, 'app_user/pages/testimonial_update.html', context)

@login_required
def privacy_update(request):
    privacy = Privacy.objects.all().last()

    if request.method == 'POST':
        privacy_form = PrivacyForm(request.POST, request.FILES, instance=privacy)
        if privacy_form.is_valid():
            privacy_form.save()
            return redirect('app_user:admin_index')
    else:
        privacy_form = PrivacyForm(instance=privacy)

    context = {'privacy':privacy, 'privacy_form':privacy_form}
    return render(request, 'app_user/pages/privacy.html', context)