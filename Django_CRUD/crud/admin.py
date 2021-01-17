from django.contrib import admin

# Register your models here.
from .models import ParcelList,DriverList

admin.site.register(ParcelList)
admin.site.register(DriverList)
