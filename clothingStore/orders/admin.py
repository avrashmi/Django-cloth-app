from django.contrib import admin
from .models import Order, OrderItems
# Register your models here.

class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra =0

class OrderAdmin(admin.ModelAdmin):
    inlines =[
        OrderItemsInline
    ]





admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItems)