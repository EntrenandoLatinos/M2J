from django import forms
from app_core.models import Contact, Banner, About, Skill, Counter, Service, SubService, Testimonial, Partner, Faq, Privacy

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['location', 'phone1', 'phone2', 'email']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'phone1': forms.TextInput(attrs={'class': 'form-control'}),
            'phone2': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}),
        }

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['image', 'title', 'subtitle', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['image', 'about', 'mision', 'vision']
        widgets = {
            'about': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
            'mision': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
            'vision': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title1', 'description1', 'title2', 'description2', 'title3', 'description3']
        widgets = {
            'title1': forms.TextInput(attrs={'class': 'form-control'}),
            'description1': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
            'title2': forms.TextInput(attrs={'class': 'form-control'}),
            'description2': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
            'title3': forms.TextInput(attrs={'class': 'form-control'}),
            'description3': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }

class CounterForm(forms.ModelForm):
    class Meta:
        model = Counter
        fields = ['title1', 'number1', 'title2', 'number2', 'title3', 'number3']
        widgets = {
            'title1': forms.TextInput(attrs={'class': 'form-control'}),
            'number1': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'title2': forms.TextInput(attrs={'class': 'form-control'}),
            'number2': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'title3': forms.TextInput(attrs={'class': 'form-control'}),
            'number3': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['image', 'title', 'description', 'description_finish']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
            'description_finish': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }

class SubServiceForm(forms.ModelForm):
    class Meta:
        model = SubService
        fields = ['service', 'image', 'title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['image', 'name', 'location', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }

class TestimonialDeleteForm(forms.Form):
    id_to_delete = forms.IntegerField(widget=forms.HiddenInput())

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['image']

class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }

class PrivacyForm(forms.ModelForm):
    class Meta:
        model = Privacy
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }