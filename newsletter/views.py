from django.shortcuts import render
import requests
import json
from django.conf import settings
from django.http import HttpResponseRedirect
from .forms import EmailSignupForm
from .models import Sign_up
# Create your views here.

MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = f'http://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'

def subscribe(email):
    data = {
        'email_address': email,
        'status': 'subscribed'
    }
    r = requests.post(
        members_endpoint,
        auth=('', MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return r.status_code, r.json()

def email_list_signup(request):
    form = EmailSignupForm(request.POST or None)
    forms = EmailSignupForm()
    if request.method == 'POST':
        if form.is_valid():
            email_signup_qs = Sign_up.objects.filter(email=form.instance.email)
            if email_signup_qs.exists():
                return render(request, 'subscribed.html', {'forms': forms})
            else:
                subscribe(form.instance.email)
                form.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
