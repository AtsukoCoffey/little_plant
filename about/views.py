from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime

from .models import AboutUs
from .forms import ContactUsForm
from profiles.models import UserProfile


def _send_confirmation_email(request, form_data):
    """
    Send the user a confirmation email for contact form submission
    """
    email = form_data['email']
    subject = render_to_string(
        'about/confirmation_emails/confirmation_email_subject.txt',
        )
    body = render_to_string(
        'about/confirmation_emails/confirmation_email_body.txt',
        {
            'contact_email': settings.DEFAULT_FROM_EMAIL,
            'form': form_data,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    )

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [email]
    )


def about_us(request):
    """
    Renders the About Page and Contact form
    Send email with "confirmation_emails"
    Reused from Checkout app
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
            _send_confirmation_email(request, form.cleaned_data)
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


def privacy_policy(request):
    """
    Renders the Privacy policy Page
    """
    return render(request, "about/privacy_policy.html")
