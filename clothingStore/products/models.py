from django.db import models

from django.db.models.signals import post_save, pre_save
from django.db.models import Sum
from django.urls import reverse
from django.utils.text import slugify


import decimal
# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=20)
    slug = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to ='category',null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(ProductCategory, on_delete= models.CASCADE)
    description = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='products',null=True, blank=True)
    marked_price = models.DecimalField(max_digits =5, decimal_places=2, default=False)
    selling_price = models.DecimalField(max_digits =5, decimal_places=2, default=False)
    slug = models.SlugField(null= True, default= True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug =slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("products:products_detail", kwargs={'slug':self.slug})


class Images(models.Model):
    image = models.ImageField(upload_to='products',null=True, blank=True)
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name='images')
    is_primary = models.BooleanField(default= False)
   
    def __str__(self):
        return str(self.product)





















