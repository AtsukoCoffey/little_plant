from django.contrib import admin
from .models import PlantItem, Category


class PlantItemAdmin(admin.ModelAdmin):
    list_display = (
        'plant_name',
        'category',
        'price',
        'average_rate',
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
