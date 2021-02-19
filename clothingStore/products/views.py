from django.shortcuts import render
from .models import ProductCategory, Product, Images
from django.views.generic import ListView, DetailView
# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'products/products_list.html'

    def get_queryset(self, *args, **kwargs):
        qs =super().get_queryset(*args, **kwargs)

        return qs.exclude(slug=None)



class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/products_detail.html'


class ProductListView1(ProductListView):
    template_name = 'products/products_detail.html'
    

