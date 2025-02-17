from django.shortcuts import render
from .models import AboutUs


def about_us(request):
    """
    Renders the About Page
    """
    about_content = AboutUs.objects.all().order_by('-created_on').first()
    return render(
        request,
        "about/aboutus.html",
        {"about_content": about_content},
    )
