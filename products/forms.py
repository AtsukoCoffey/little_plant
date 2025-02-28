from django import forms
from .widgets import CustomClearableFileInput
from .models import PlantItem, Category, ReviewRating


class ProductForm(forms.ModelForm):
    class Meta:
        model = PlantItem
        fields = ('name', 'scientific_name', 'category', 'description',
                  'image_url', 'image', 'price', 'sale_price')

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # List comprehension - tie ID and friendly name in this variable
        friendly_names = [('', 'Non category')] + [
            (c.id, c.get_friendly_name()) for c in categories
        ]
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
        self.fields['image'].widget.attrs['aria-label'] = 'Select image'


class ReviewForm(forms.ModelForm):
    """
    Form to leave a review on the product. :model products.ReviewRating
    """
    class Meta:
        model = ReviewRating
        fields = ('review_body', 'image')
        widgets = {
            'review_body': forms.Textarea(attrs={'rows': 3}),
        }
    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
