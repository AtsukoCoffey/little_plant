from django.views.generic import CreateView
from django.contrib import messages

from .models import NewsLetter


class NewsLetterCreateView(CreateView):
    template_name = "newsletter/news_letter_form.html"
    model = NewsLetter
    fields = ['email',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(
            self.request,
            "Thanks for subscribing to our newsletter!"
            )
        return super(NewsLetter, self).form_valid(form)
