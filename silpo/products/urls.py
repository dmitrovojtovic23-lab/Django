from django.urls import path
from . import views
from .create_views import create_product

app_name='products'

urlpatterns = [
    path('', views.show_products, name='show_products'),
    path('create/', create_product, name='create_product'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
]