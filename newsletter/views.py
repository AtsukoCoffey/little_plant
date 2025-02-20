from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import NewsLetterForm
from profiles.models import UserProfile


def NewsLetterCreateView(request):
    """
    Renders the Newsletter subscriotion Page
    """
    success_message = 'Thanks for subscribing to our newsletter! '\
        'We send you e-mail address confirmation mail. '\
        'Please check your e-mail.'

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            form = NewsLetterForm(initial={
                'email': profile.user.email,
            })
        except UserProfile.DoesNotExist:
            form = NewsLetterForm()

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, success_message)
            return redirect('home')

    context = {
            "form": form,
    }
    return render(request, "newsletter/news_letter_form.html", context)
