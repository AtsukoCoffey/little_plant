from django.views.generic import CreateView
from django.contrib import messages

from .models import NewsLetter


class NewsLetterCreateView(CreateView):
    model = NewsLetter
    fields = ['email',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.info(
            self.request,
            "Thanks for subscribing to our newsletter!"
            " Be on the lookout for exciting news from"
            " Web Piano Academy!"
            )
        return super(NewsLetter, self).form_valid(form)
