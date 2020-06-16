from django.http import HttpResponse
from django.shortcuts import render


# /products -> index
# Uniform Resource Locator (Address)
def index(request):
    return HttpResponse('Hello World213')


def new(request):
    return HttpResponse('New Products')