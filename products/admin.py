from django.contrib import admin
from .models import PlantItem, Category


class PlantItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'sale_price',
        'rating',
        'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(PlantItem, PlantItemAdmin)
admin.site.register(Category, CategoryAdmin)
