from django.shortcuts import render
from .models import Product

# Create your views here.

def p_list(request):
    
    products = Product.objects.all()
    
    return render(request, 'products.html', {'products': products})

def cart(request, pid):
    # Product.make_order(pid)
    products = Product.objects.filter(id=pid).update(p_cout = p_cout-1)
    products = Product.objects.filter(id=pid)
    return render(request, 'cart.html', {'products': products})