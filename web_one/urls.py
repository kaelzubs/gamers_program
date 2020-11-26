from django.urls import path, re_path
from . import views
from .views import StaticViewSitemap, search_view
from django.contrib.sitemaps.views import sitemap


sitemaps = {

    'static': StaticViewSitemap,
}



urlpatterns = [
    path('', views.home_view, name='home'),
    path('search/', views.search_view, name='search'),
    path('xbox/', views.xbox_view, name='xbox'),
    path('playstation/', views.playstation_view, name='playstation'),
    path('nitendo/', views.nintendo_view, name='nintendo'),
    path('accessories/', views.accessories_view, name='accessories'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('disclaimer/', views.disclaimer_view, name='disclaimer'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
