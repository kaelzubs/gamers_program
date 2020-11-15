from django.contrib import admin
from . models import Sign_up

# Register your models here.

class SignupAdmin(admin.ModelAdmin):
    search_fields = ('email',)
admin.site.register(Sign_up, SignupAdmin)
