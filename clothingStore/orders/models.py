from django.db import models
from products.models import Product
from django.db.models.signals import post_save, pre_save, pre_delete
from django.db.models import Sum
from inventory.models import Stock
from django.core.exceptions import ValidationError
# Create your models here.
ORDER_STATUS =[
    (0,'cart'),
    (1,'paid'),
    (2,'refunded'),
    (3,'shift'),
    (4,'delivered'),
]


class Order(models.Model):
    subtotal = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    totalTax = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    order =models.IntegerField(default=0, choices=ORDER_STATUS)

    def __str__(self):
        return str(self.id)
    

    

class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    line_total = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.product)


    def save(self, *args, **kwargs):
        self.line_total = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def clean(self):
        stock = Stock.objects.filter(product = self.product)
        if stock.exists():
            stock =stock.first()
            if stock.inventory < self.quantity:
                raise ValidationError({'quantity':f'max available:{stock.inventory}'})
        else:
            raise ValidationError({'quantity':'Sufficient quantity not available'})



def post_save_OrderItems(sender, instance, *args, **kwargs):
    order = instance.order
    ordered_items = order.items.aggregate(order_total =Sum('line_total'))
    order.subtotal = ordered_items['order_total']
    order.save()

    stock =Stock.objects.filter(product = instance.product)
    if stock.exists():
        stock = stock.first()
        stock.inventory -= instance.quantity
        
        stock.save()

post_save.connect(post_save_OrderItems, sender=OrderItems)

def pre_save_OrderItems(sender, instance, *args, **kwargs):
    order = instance.order

    if instance.id is not None:
        stock = Stock.objects.filter(product =instance.product)
        if stock.exists():
            stock = stock.first()
            pre_orderItems =OrderItems.objects.get(id= instance.id)
            
            stock.inventory += pre_orderItems.quantity
            stock.save()
    
pre_save.connect(pre_save_OrderItems, sender=OrderItems)
pre_delete.connect(pre_save_OrderItems, sender=OrderItems)

















