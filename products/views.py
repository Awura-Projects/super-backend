from itertools import product
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.


def product_list(request):
    context = {'product_list': Product.objects.all()}
    return render(request, "product_register/product_list.html", context)


def products_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(instance=product)
        return render(request, "product_register/products_form.html", {'form': form})
    else:
        if id == 0:
            form = ProductForm(request.POST)
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(request.POST,instance= product)
        if form.is_valid():
            form.save()
        return redirect('/products/list')

def product_delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('/product/list')
