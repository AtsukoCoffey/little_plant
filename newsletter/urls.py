from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsLetterCreateView, name='news-letter-subsc'),
]
