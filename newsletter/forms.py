from django import forms
from .models import Sign_up


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': 'email',
        'name': 'email',
        'id': 'email',
        'placeholder': 'Enter your e-mail address',
        'class': 'newsletter-inner'
    }), label='')

    class Meta:
        model = Sign_up
        fields = ('email',)



