from django.contrib import admin
from .models import ProductCategory, Product, Images
from inventory.models import Receiving, Stock
# Register your models here.

class ReceivingInline(admin.TabularInline):
    model =Receiving
    extra =0

class StockInline(admin.TabularInline):
    model =Stock
    extra =0

class ProductAdmin(admin.ModelAdmin):
    inlines =[
        ReceivingInline, StockInline
    ]

admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)
