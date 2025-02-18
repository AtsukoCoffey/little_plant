from django.contrib import admin
from .models import AboutUs
from django_summernote.admin import SummernoteModelAdmin


@admin.register(AboutUs)
class AboutUsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
