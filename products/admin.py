from django.contrib import admin
from .models import PlantItem


class PlantItemAdmin(admin.ModelAdmin):
    list_display = (
        'plant_name',
        'category',
        'price',
        'average_rate',
        'image',
    )

    # ordering = ('category')


admin.site.register(PlantItem, PlantItemAdmin)
