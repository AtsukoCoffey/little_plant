from django.shortcuts import render, get_object_or_404
from .models import PlantItem


def all_products(request):
    """ A view to show all products"""
    products = PlantItem.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, slug):
    """ 
    A view to show individual product details
    Display an individual product :model:`products.PlantItem`.

    **Context**
    
    """
    product = get_object_or_404(PlantItem, slug=slug)
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
