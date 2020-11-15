from django.urls import path
from .views import cookie_policy


urlpatterns = [
    path('configuration/', cookie_policy, name='cookie-list'),
]