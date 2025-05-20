from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>مرحبًا بك في المتجر الرقمي 🛒</h1>")
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})