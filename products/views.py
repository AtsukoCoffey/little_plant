from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import PlantItem, Category, ReviewRating
from .forms import ProductForm, ReviewForm


# For update the result anytime - independent function
def get_user_rating(user, product):
    if user.is_authenticated:
        rating = ReviewRating.objects.get(
            product=product, reviewer=user)
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
            special_offer = products.filter(sale_price__isnull=False)
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
    model:`products.PlantItem`, 'products.ReviewRating'
    **Context**
    'product': Indivisual product detail
    'reviews': All the reviews related to thid indivisual product
    "review_form": Check if user already has write review, populate or newform
    """
    product = get_object_or_404(PlantItem.objects.all(), slug=slug)
    # Get all reviews for list view
    reviews = product.reviews.all().order_by("-created_on")

    # For preventing to create multiple reviews per user
    # Even 'Create' button works like 'Edit'
    # Populate existing own review to the form
    if request.user.is_authenticated:
        try:
            review_instance = ReviewRating.objects.get(
                reviewer=request.user, product=product
            )
            review_form = ReviewForm(instance=review_instance)
        except ReviewRating.DoesNotExist:
            review_form = ReviewForm()
    else:
        review_form = ReviewForm()

    # POST request for review : only authenticated user can do
    if request.method == "POST" and request.user.is_authenticated:
        review_form = ReviewForm(
            request.POST,
            # with "review_instance" > assigned in try statement
            instance=review_instance if 'review_instance' in vars() else None
        )
        # Star rating value
        rating = request.POST.get('rate')

        # form validation
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product
            review.reviewer = request.user
            review.rating = rating
            review.save()
            messages.success(
                request, 'Review Updated!'
            )
            # Clear the form
            review_form = ReviewForm()
            return render(request, 'products/product_detail.html', {
                'product': product,
                'reviews': reviews,
                "review_form": review_form,
            })
        else:
            messages.add_message(
                request, messages.error, 'Error updating review!')

    context = {
        'product': product,
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
        messages.error(request, 'Sorry, only owner or stuff can add products.')
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
        messages.error(
            request, 'Sorry, only owner or stuff can edit products.'
        )
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


@login_required
def review_edit(request, slug, review_id):
    """
    Indivisual review for edit
    `review_id`arg is sent from template, reverse relation of `reviews`
    """
    product = get_object_or_404(PlantItem.objects.all(), slug=slug)
    review = get_object_or_404(ReviewRating, pk=review_id)
    review_form = ReviewForm(data=request.POST, instance=review)

    # Check the review is request user's review
    if request.method == "POST" and review.reviewer == request.user:
        review_form = ReviewForm(data=request.POST, instance=review)

        # form validation
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product
            review.save()
            messages.success(
                request, 'Review Updated!'
            )
        else:
            messages.success(
                request, 'Error updating review!')
    return HttpResponseRedirect(reverse('product_detail', args=[slug]))


@login_required
def review_delete(request, slug, review_id):
    """
    Delete an individual review.
    **Context**
    """
    # product = get_object_or_404(PlantItem.objects.all(), slug=slug)
    review = get_object_or_404(ReviewRating, pk=review_id)

    #  "user = reviewer" check
    if review.reviewer == request.user:
        review.delete()
        messages.success(
            request, 'Your review is deleted!'
        )
    else:
        messages.error(
            request, 'You can only delete your own reviews!')
    return HttpResponseRedirect(reverse('product_detail', args=[slug]))


def review(request):

    context = {
        'reviews': ReviewRating.objects.all(),
        'all_categories': Category.objects.all(),
    }

    if request.GET:
        if request.GET['category']:
            category = request.GET['category'].split(',')
            reviews = ReviewRating.objects.filter(
                product__category__name__in=category
            )
            context = {
                'reviews': reviews,
                'category': category[0],
                'all_categories': Category.objects.all(),
            }
        else:
            context = {
                'reviews': reviews,
                'all_categories': Category.objects.all(),
            }

    return render(request, 'products/review.html', context)
