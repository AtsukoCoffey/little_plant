from django.shortcuts import render

from .models import Faq, FaqCategory


def faq(request):

    faqs = Faq.objects.all()
    # return category list for quick access links
    category_list = FaqCategory.objects.all()

    if request.GET:
        category = request.GET['category']
        faqs = Faq.objects.filter(category=category)
        category = FaqCategory.objects.filter(pk=category)

    context = {
        'faqs': faqs,
        'category': category[0],
        'category_list': category_list,
    }

    return render(request, 'faq/faq.html', context)
