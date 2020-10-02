from django.contrib import admin

# Register your models here.
from unesco.models import Sites, Category, Region, Iso, States

admin.site.register(Sites)
admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Iso)
admin.site.register(States)

