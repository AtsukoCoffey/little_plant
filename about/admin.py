from django.contrib import admin
from .models import AboutUs, ContactUs, ContactPurpose
from django_summernote.admin import SummernoteModelAdmin


@admin.register(AboutUs)
class AboutUsAdmin(SummernoteModelAdmin):
    """
    Register the model into admin site. Instead of admin.site.register(AboutUs)
    @admin decorator, class based model to use Summernote.
    """
    summernote_fields = ('content',)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """
    Register Contact us message model into admin site.
    """
    list_display = (
        'user_name',
        'email',
        'message',
        'purpose',
        'checked',
    )

admin.site.register(ContactPurpose)