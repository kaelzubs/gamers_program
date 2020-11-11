from django.contrib import admin
from .models import HomeModel, TrendModel, RelatedModel

# Register your models here.
admin.site.register(HomeModel)
admin.site.register(TrendModel)
admin.site.register(RelatedModel)
