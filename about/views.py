from django.shortcuts import render, redirect
from django.contrib import messages

from .models import AboutUs
from .forms import ContactUsForm
from profiles.models import UserProfile


def about_us(request):
    """
    Renders the About Page and Contact form
    """
    about_content = AboutUs.objects.all().order_by('-created_on').first()
    form = ContactUsForm()
    success_message = 'Your message has been successfully sent!' \
        'Thank you for contact us.  We will review your message soon' \
        ' and respond shortly.'

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, success_message)
            return redirect('about')

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            form = ContactUsForm(initial={
                'user_name': profile.user.username,
                'email': profile.user.email,
            })
        except UserProfile.DoesNotExist:
            form = ContactUsForm()
    else:
        form = ContactUsForm()

    context = {
        "about": about_content,
        "form": form,
    }
    return render(request, "about/aboutus.html", context)
