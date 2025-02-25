from django.urls import path

from . import views

urlpatterns = [
    path('', views.about_us, name='about'),
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),
]
