from django.contrib import admin
from .models import Restaurant, Location, Menu, Category, MenuItem

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Location)
admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(MenuItem)