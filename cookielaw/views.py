from django.shortcuts import render
# Create your views here.


def cookie_policy(request):
        
    return render(request, 'cookielaw/cookie_page.html')