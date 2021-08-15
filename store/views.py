from django.http.response import HttpResponse
from django.shortcuts import render

def home(req):
    return render(req, 'store/index.html')

def product(req):
    return render(req, 'store/products.html')

def about(req):
    return render(req, 'store/about.html')

def contact(req):
    return render(req, 'store/contact.html')