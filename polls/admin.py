from django.contrib import admin
from .models import City, Price, Good

admin.site.register(City)
admin.site.register(Good)
admin.site.register(Price)

# Register your models here.
