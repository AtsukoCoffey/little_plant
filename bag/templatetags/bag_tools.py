from django import template

# Custom templates and Tags => django doc
# To register this filter need to create a variable "register"
# Assign to template.Library
register = template.Library()
# This takes in a price and a quantity as parameters and simply returns
# their product.
# Register filter decorator to register function as a template filter.
# Django doc: custom template tags and filter


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
