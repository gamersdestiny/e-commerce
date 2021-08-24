from django.http import request
from django.shortcuts import render
from .models import Basket
def basket(request):
    context = {
        'basket': Basket.objects.all(),
        'total': Basket.sub_total
    }
    return render(request, 'basket/basket.html', context)
