from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import AboutUs, ContactUs, ContactPurpose


class AboutUsForm(forms.ModelForm):
    """
    Summernote is for admin user to update About us contents
    """
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = AboutUs
        fields = '__all__'


class ContactUsForm(forms.ModelForm):
    """
    Contact form
    """
    # Set the purpose FK into select option
    purpose = forms.ModelChoiceField(
        queryset=ContactPurpose.objects.all(),
        empty_label="Select a purpose",
        required=False
    )

    class Meta:
        model = ContactUs
        fields = ['user_name', 'email', 'purpose', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        purpose = ContactPurpose.objects.all()
