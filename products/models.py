from django.db import models
from django.db.models import Avg
from django.utils.text import slugify
from django_resized import ResizedImageField

from django.contrib.auth.models import User


class Category(models.Model):
    """
    Product categories. Related to :model:`PlantItem`
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class PlantItem(models.Model):
    """
    Product item model.
    Related to :model:`Category`
    Also for average rating :model:`ReviewRating`
    """
    name = models.CharField(
        max_length=100, unique=True, null=False, blank=False
    )
    scientific_name = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField()
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=500)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = ResizedImageField(
        size=[400, None], quality=75, upload_to="products",
        force_format='WEBP', blank=True
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PlantItem, self).save(*args, **kwargs)

    def average_rating(self) -> float:
        return ReviewRating.objects.filter(
            product=self).aggregate(Avg("rating"))["rating__avg"] or 0


class ReviewRating(models.Model):
    """
    Stores review and rating values for each customer by product
    Related to :model:`auth.User` and products :model:`PlantItem`
    """
    product = models.ForeignKey(
        PlantItem, on_delete=models.CASCADE, related_name="reviews", null=False
    )
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviewer', null=False
    )
    review_body = models.CharField(max_length=500, null=False, blank=False)
    image = ResizedImageField(
        size=[250, None], quality=75, upload_to="reviews",
        force_format='WEBP', blank=True
    )
    created_on = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0, null=True)

    def __str__(self):
        return f"{self.product.name}: {self.rating}"
