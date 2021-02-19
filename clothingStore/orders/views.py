from django.shortcuts import render
from .models import Order, OrderItems
from django.views.generic import ListView, DetailView
# Create your views here.

class OrderView(ListView):
    model = OrderItems
    template_name= 'orders/orders.html'


