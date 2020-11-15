from django.shortcuts import render
from django.db.models import Q
from . models import cookie_Page
# Create your views here.

def cookie_policy(request):
    pages = cookie_Page.objects.order_by('-created')
    if request.user.is_staff or request.user.is_superuser:
        pages = cookie_Page.objects.all().order_by('-created')

    query = request.GET.get('q')
    if query:
        pages = cookie_Page.objects.filter(
            Q(title__icontains=query) |
            Q(bodytext__icontains=query) |
            Q(created__icontains=query)
        ).distinct()


    return render(request, 'cookielaw/cookie_page.html', {'forms': forms, 'pages': pages})