from django.shortcuts import render, get_object_or_404

from products.models import Product


# Create your views here.
def show_products(request):
    products = Product.objects.prefetch_related("images").all()
    return render(request, "products.html", {"products": products})


def product_detail(request, pk):
    product = get_object_or_404(Product.objects.prefetch_related("images"), pk=pk)
    return render(request, "product_detail.html", {"product": product})
 