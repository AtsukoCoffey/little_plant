from django.urls import path
from . import views
from .views import NewsLetterCreateView

urlpatterns = [
    path('', NewsLetterCreateView.as_view(), name='news-letter-subsc'),
]
