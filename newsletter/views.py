from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import NewsLetterForm
from profiles.models import UserProfile


def NewsLetterCreateView(request):
    """
    Renders the Newsletter subscriotion Page
    """
    form = NewsLetterForm
    success_message = 'Thanks for subscribing to our newsletter!' \
        'We will send you shortly'
    
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            form = NewsLetterForm(initial={
                'email': profile.user.email,
            })
        except UserProfile.DoesNotExist:
            form = NewsLetterForm()

    context = {
            "form": form,
    }
    return render(request, "newsletter/news_letter_form.html", context)
