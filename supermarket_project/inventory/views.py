# inventory/views.py

from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def home(request):
    products = Product.objects.all()
    return render(request, 'inventory/home.html', {'products': products})  # 修正路径

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})  # 修正路径

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'inventory/delete_product.html', {'product': product})  # 修正路径