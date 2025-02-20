from django.db import models


class AboutUs(models.Model):
    """
    About Us contents. - Site owner can update using admin panel
    """
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactPurpose(models.Model):
    """
    Contact form - purpose
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    """
    Contact form - main form
    Related to (FK) :ContactPurpose
    """
    user_name = models.CharField(max_length=255,)
    email = models.EmailField()
    message = models.TextField()
    checked = models.BooleanField(default=False)
    purpose = models.ForeignKey(
        'ContactPurpose', null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.user_name}"
