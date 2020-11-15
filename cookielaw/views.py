from django.shortcuts import render
from . models import cookie_Page
# Create your views here.

def cookie_policy(request):
    pages = cookie_Page.objects.order_by('-id')
    if request.user.is_staff or request.user.is_superuser:
        pages = cookie_Page.objects.all().order_by('-id')
        

    return render(request, 'cookielaw/cookie_page.html', {'pages': pages})