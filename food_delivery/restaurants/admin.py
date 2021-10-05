from django.contrib import admin
from .models import Cuisine,Restaurant,Address,Dish

# Register your models here.
admin.site.register(Cuisine)
admin.site.register(Restaurant)
admin.site.register(Address)
admin.site.register(Dish)
