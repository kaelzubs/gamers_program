from django.contrib import admin
from . models import cookie_Page


# Register your models here.

class CookieAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

    fieldsets = [
        ("Title/date", {'fields': ["title", "created"]}),
    ]

admin.site.register(cookie_Page, CookieAdmin)
