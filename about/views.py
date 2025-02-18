from django.shortcuts import render, redirect
from django.contrib import messages

from .models import AboutUs
from .forms import ContactUsForm


def about_us(request):
    """
    Renders the About Page and Contact form
    """
    about_content = AboutUs.objects.all().order_by('-created_on').first()
    form = ContactUsForm()

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully send a contact form!')
            return redirect('about')

    context = {
        "about": about_content,
        "form": form,
    }
    return render(request, "about/aboutus.html", context)
