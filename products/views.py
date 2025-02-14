from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import PlantItem, Category
from .forms import ProductForm


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
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey  # store in the global variable
            if sortkey == 'name':
                sortkey = 'lower_name'  # Assign into new field
                products = products.annotate(lower_name=Lower('name'))
                # Added lower_name field in the Prouct
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            # Category is FK of products so access to Category name
            products = products.filter(category__name__in=category)
            # For current category
            category = Category.objects.filter(name__in=category)

        if 'sale_price' in request.GET:
            special_offer = products.exclude(sale_price__icontains=0)
            products = special_offer

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query
            ) | Q(
                description__icontains=query
            )
            products = products.filter(queries)

    # return current sorting methodology to the template
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
        'current_sorting': current_sorting,
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


def add_product(request):
    """
    Add a product to the store. Site owner or administrator only
    model:`products.PlantItem`

    **Context**

    """
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'on_product_page': True,
    }

    return render(request, template, context)
