from django.shortcuts import render,HttpResponse
from .models import Product

# Create your views here.

def product_list(request):
    products=Product.objects.all()
    return render(request,'products.html',{'products': products})


