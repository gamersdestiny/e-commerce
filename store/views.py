from django.shortcuts import render 
from . import models


def home(req):
    context = {
        'product' : models.Product.objects.all()
    }
    return render(req, 'store/home.html', context)


def product(req, slug):
    context = {
        'detail': models.Product.objects.get(slug=slug)
    }
    return render(req, 'store/products.html', context)


def about(req):
    return render(req, 'store/about.html')


def contact(req):
    return render(req, 'store/contact.html')
