from django.contrib import admin
from . models import Meal, MealLink
from mptt.admin import MPTTModelAdmin

# Register your models here.
admin.site.register(Meal, MPTTModelAdmin)
admin.site.register(MealLink)