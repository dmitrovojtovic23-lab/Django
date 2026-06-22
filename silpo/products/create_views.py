from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from products.models import ProductImage
from .forms import ProductForm


@login_required
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            image_file = form.cleaned_data.get("image")
            if image_file:
                ProductImage.objects.create(product=product, image=image_file, priority=0)
            return redirect('products:show_products')
    else:
        form = ProductForm()

    return render(request, "create_product.html", {"form": form})
