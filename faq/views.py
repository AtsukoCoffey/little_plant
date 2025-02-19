from django.shortcuts import render

from .models import Faq, FaqCategory


def faq(request):

    faqs = Faq.objects.all()

    if request.GET:
        category = request.GET['category']
        faqs = Faq.objects.filter(category=category)
        category = FaqCategory.objects.filter(pk=category)

    context = {
        'faqs': faqs,
        'category': category[0],
    }

    return render(request, 'faq/faq.html', context)
