from django.db import models

from products.models import Product
from django.db.models.signals import post_save, pre_save

# Create your models here.

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    inventory = models.IntegerField(default =0)

    def __str__(self):
        return str(self.product)


class Receiving(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default =0)

    def __str__(self):
        return str(self.product)

def post_save_Receiving(sender, instance, *args, **kwargs):
    product = instance.product
    stock =Stock.objects.filter(product=product)
    if stock.exists():
        stock = stock.first()
        stock.inventory += instance.quantity
        stock.save()
    else:
        Stock.objects.create(product=product, inventory=instance.quantity) 

post_save.connect(post_save_Receiving, sender=Receiving)


def pre_save_Receiving(sender, instance, *args, **kwargs):
    product = instance.product
    if instance.id is not None:
        stock = Stock.objects.filter(product=product)
        stock = stock.first()
        pre_receiving = Receiving.objects.get(id = instance.id)
        stock.inventory -= pre_receiving.quantity
        stock.save()

pre_save.connect(pre_save_Receiving, sender=Receiving)







