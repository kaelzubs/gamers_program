from django import forms
from .models import ContactModel

class ContactForms(forms.ModelForm):
    name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'name',
        'placeholder': '',
        'class': 'form-group'
    }))
    
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'type': 'email',
        'name': 'email',
        'placeholder': '',
        'class': 'form-group'
    }))
    
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'subject',
        'placeholder': '',
        'class': 'form-group'
    }))
    
    phone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'company_name',
        'placeholder': '',
        'class': 'form-group'
    }))
    
    message = forms.CharField(widget=forms.Textarea(attrs={
        'name': 'message',
        'placeholder': '',
        'class': 'form-group message'
    }))
    
    
    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'subject', 'phone', 'message')
    
