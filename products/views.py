from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import PlantItem, Category


def all_products(request):
    """
    A view to show all products
    model:`products.PlantItem`

    **Context**

    """
    products = PlantItem.objects.all()
    query = None
    category = None
    special_offer = None

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            # Category is FK of products so access to Category name
            products = products.filter(category__name__in=category)
            # For current category
            category = Category.objects.filter(name__in=category)

        if 'sale_price' in request.GET:
            special_offer = products.exclude(sale_price__icontains=0)
            print(special_offer)
            products = special_offer

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = Q(
                plant_name__icontains=query
            ) | Q(
                description__icontains=query
            )
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, slug):
    """
    A view to show individual product details
    model:`products.PlantItem`

    **Context**

    """
    product = get_object_or_404(PlantItem, slug=slug)
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
