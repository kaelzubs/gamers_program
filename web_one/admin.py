from django.contrib import admin
from .models import HomeModel, TrendModel, RelatedModel, Accessories, Nintendo, Xbox, Playstation, Search

# Register your models here.
admin.site.register(HomeModel)
admin.site.register(TrendModel)
admin.site.register(RelatedModel)
admin.site.register(Accessories)
admin.site.register(Nintendo)
admin.site.register(Xbox)
admin.site.register(Playstation)
admin.site.register(Search)

