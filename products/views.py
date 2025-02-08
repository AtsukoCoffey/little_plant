from django.shortcuts import render
from .models import PlantItem


def all_products(request):
    """ A view to show all products"""
    products = PlantItem.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
