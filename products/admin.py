from django.contrib import admin
from .models import PlantItem, Category, ReviewRating


class PlantItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'sale_price',
        'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'reviewer',
        'image',
        'created_on',
    )


admin.site.register(PlantItem, PlantItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
