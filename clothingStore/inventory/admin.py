from django.contrib import admin
from .models import Stock, Receiving
# Register your models here.





class StockAdmin(admin.ModelAdmin):
    list_display =['product', 'inventory']
    readonly_fields =['inventory']







admin.site.register(Stock, StockAdmin)
admin.site.register(Receiving)

