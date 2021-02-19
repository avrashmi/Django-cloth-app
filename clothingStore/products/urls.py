from django.urls import path
from .views import ProductListView, ProductDetailView
app_name ='products'

urlpatterns =[
    path('products/', ProductListView.as_view(), name='products'),
    path('product_detail/<slug:slug>/', ProductDetailView.as_view(), name='products_detail'),
    
]


