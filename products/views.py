from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import PlantItem, Category, ReviewRating
from .forms import ProductForm, ReviewForm


# For update the result anytime - independent function
def get_user_rating(user, product):
    if user.is_authenticated:
        rating = ReviewRating.objects.filter(product=product, reviewer=request.user).first()
        return rating.rating if rating else 0
    else:
        return 0


def all_products(request):
    """
    A view to show all products
    model:`products.PlantItem`

    **Context**
    'products': all products, or filtered products
    'search_term': matched data that was included in name, description field
    'current_category': send the category name that was used for the filter
    'current_sorting': send the sorting type and direction (asc, dec)
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
    This page's url is constructed by slug to prevent to guess the other pages
    model:`products.PlantItem`
    **Context**
    'product': indivisual product detail
    """
    product = get_object_or_404(PlantItem.objects.all(), slug=slug)

    # Review part - get user's own rating value function
    user_rating = get_user_rating(request.user, product)
    # get all reviews for this product
    reviews = product.reviews.all().order_by("-created_on")
    review_form = ReviewForm()

    context = {
        'product': product,
        'user_rating': user_rating,
        'reviews': reviews,
        "review_form": review_form,
    }

    return render(request, 'products/product_detail.html', context)


# @login_required
def add_product(request):
    """
    Add a product to the store. Site owner or administrator only
    Non superuser is redirected to login page
    model:`products.PlantItem`
    **Context**
    'form': `products.PlantItem`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('account_login'))

    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # To access this instance id, assign this form.save()
            product = form.save()
            messages.success(request, 'Successfully added product!')
            # After adding the product redirect to details page
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# @login_required
def edit_product(request, product_id):
    """
    Edit a product in the store. Site owner or administrator only
    Non superuser is redirected to login page
    model:`products.PlantItem`
    **Context**
    'form': `products.PlantItem`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('account_login'))

    product = get_object_or_404(PlantItem, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

        template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """
    Delete a product from the store. Site owner or administrator only
    Non superuser is redirected to login page
    model:`products.PlantItem` - indivisual product_id page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('account_login'))

    product = get_object_or_404(PlantItem, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
