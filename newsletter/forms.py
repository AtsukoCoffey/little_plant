from django import forms
from .models import NewsLetter


class NewsLetterForm(forms.ModelForm):
    """
    Form to subscribe newsletter
    """
    class Meta:
        model = NewsLetter
        fields = ('email',)
