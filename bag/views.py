from django.shortcuts import render, redirect, reverse, HttpResponse


def view_bag(request):
    """
    A view that renders the bag contents page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified product to the shopping bag
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # access bag in context_processors
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    # Overwrite the shopping bag
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount
    """
    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity  # update the quantity
    else:   # quantity is 0
        bag.pop(item_id)  # Or delete entirely with pop

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))  # back to view_bag


def remove_from_bag(request, item_id):
    """
    Remove the item from the shopping bag
    """
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
