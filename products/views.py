from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# /products -> index
# Uniform Resource Locator (Address)
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
# Object, template, context: a dictionary that contains data to be pass to the template


def new(request):
    return HttpResponse('New Products')