from django.contrib import admin

from .models import Product, Feature

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  
  list_display = ['name', 'specification','project','location', 'available_units']



@admin.register(Feature)
class FeaturesAdmin(admin.ModelAdmin):

    pass
  
