from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
