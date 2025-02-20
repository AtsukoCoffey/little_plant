from django.db import models
from django.shortcuts import reverse


class NewsLetter(models.Model):
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('home')
