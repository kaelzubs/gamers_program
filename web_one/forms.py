from django import forms
from .models import ContactModel

class ContactForms(forms.ModelForm):
    name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'name',
        'placeholder': '',
        'class': '.form-main. form .row .col-lg-6 col-12 .form-group'
    }), label='Your Name')
    
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'type': 'email',
        'name': 'email',
        'placeholder': '',
        'class': '.fom-main .form .row .col-lg-6 col-12 .form-group'
    }), label='Your Email')
    
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'subject',
        'placeholder': '',
        'class': '.form-main .form .row .col-lg-6 col-12 .form-group'
    }), label='Your Subjects')
    
    phone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'company_name',
        'placeholder': '',
        'class': '.form-main .form .row .col-lg-6 col-12 .form-group'
    }), label='Your Phone')
    
    message = forms.CharField(widget=forms.Textarea(attrs={
        'name': 'message',
        'placeholder': '',
        'class': '.form-main .form .row .col-12 .form-group message'
    }), label='Your Message')
    
    
    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'subject', 'phone', 'message')
    
