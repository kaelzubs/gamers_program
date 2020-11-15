from django import forms
from .models import Sign_up


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': 'email',
        'name': 'email',
        'id': 'email',
        'placeholder': 'Enter your e-mail address',
        'class': 'newsletter-email form-control ml-2 mr-sm-2'
    }), label='')

    class Meta:
        model = Sign_up
        fields = ('email',)



