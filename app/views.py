from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.

def base(request):
    return render(request, "base.html")


#homepage view
def homepage(request):
    products=Product.objects.all()
    return render(request, 'homepage.html', {'products': products})


#product views
def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)  # Fetch the product from the database
    return render(request, 'product.html', {'product': product})