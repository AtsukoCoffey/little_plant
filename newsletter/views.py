from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import NewsLetterForm
from profiles.models import UserProfile


def _send_confirmation_email(request):
    """
    Send the user a confirmation email for newsletter
    """
    email = request.POST.get('email')
    subject = render_to_string(
        'newsletter/confirmation_emails/confirmation_email_subject.txt',
        )
    body = render_to_string(
        'newsletter/confirmation_emails/confirmation_email_body.txt',
        {'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [email]
    )


def NewsLetterCreateView(request):
    """
    Renders the Newsletter subscriotion Page
    Send email with "confirmation_emails"
    Reused from Checkout app
    """
    success_message = 'Thanks for subscribing to our newsletter! '\
        'We have sent an email to your address. '\
        'We will send newsletters shortly.'

    # Try prefill the user's email
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            form = NewsLetterForm(initial={
                'email': profile.user.email,
            })
        except UserProfile.DoesNotExist:
            form = NewsLetterForm()
    else:
        form = NewsLetterForm()

    # User submit POSt
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            _send_confirmation_email(request)
            messages.success(request, success_message)
            return redirect('home')

    context = {
            "form": form,
    }
    return render(request, "newsletter/news_letter_form.html", context)
