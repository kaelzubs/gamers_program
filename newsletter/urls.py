from django.urls import path
from .views import email_list_signup


urlpatterns = [
    path('page/', email_list_signup, name='email_list'),
]
