from django.contrib import admin
from .models import Soup, Meal, Ingredients

# Register your models here.

admin.site.register(Soup)
admin.site.register(Meal)
admin.site.register(Ingredients)