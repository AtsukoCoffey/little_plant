from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Category, PlantItem, ReviewRating
from django.utils import timezone


class TestCategory(TestCase):
    """Test the Category model"""

    def setUp(self):
        """Sample Category"""
        name = 'test_category'
        friendly_name = 'test_friendly_name'
        # instance
        category1 = Category.objects.create(
            name=name,
            friendly_name=friendly_name
        )
        category1.save()

    def test_str(self):
        """Test the string method"""
        category1 = Category.objects.latest('pk')
        category_string = str(category1.name)

        self.assertEqual((category_string), (category1.name))


class ReviewRatingTestCase(TestCase):
    """Test the review and rating model"""
    def setUp(self):
        """Sample review and rating pbject"""
        # Create a user - FK
        self.user = User.objects.create_user(username='testuser',
                                             password='12345')
        # Create a plant item - FK
        self.plant = PlantItem.objects.create(
            name='Test Plant',
            scientific_name='Testus plantus',
            description='A test plant',
            price=10.00
        )
        # instance1
        self.review1 = ReviewRating.objects.create(
            product=self.plant,
            reviewer=self.user,
            review_body='test_something_review',
            created_on=timezone.now(),
            rating=5
        )
        self.review1.save()
        # instance
        self.review2 = ReviewRating.objects.create(
            review_body='test_something_defferent_review',
            created_on=timezone.now(),
            rating=3
        )
        self.review2.save()

    def test_str(self):
        """Test the string method"""
        review_string = f"{self.plant.name}: {self.review1.rating}"
        self.assertEqual("Test Plant: 5", review_string)

    def test_review_creation(self):
        self.assertEqual(ReviewRating.objects.count(), 2)
        self.assertEqual(self.review1.product, self.plant)
        self.assertEqual(self.review1.reviewer, self.user)

    def test_rating_range(self):
        with self.assertRaises(ValidationError):
            ReviewRating.objects.create(
                product=self.plant,
                reviewer=self.user,
                review_body='invalid_rating',
                created_on=timezone.now(),
                rating=6  # Assuming rating should be 1-5
            )


class TestPlantItem(TestCase):
    """Test the product model"""
    def setUp(self):
        """Sample product object"""
        name = 'test_plant'
        scientific_name = 'test_scientific_name'
        description = 'test_description'
        price = 5.5
        # instance
        product1 = PlantItem.objects.create(
            name=name,
            scientific_name=scientific_name,
            description=description,
            price=price
        )
        product1.save()

    def test_str(self):
        """Test the string method"""
        product1 = PlantItem.objects.latest('pk')
        product_string = str(product1.name)

        self.assertEqual((product_string), (product1.name))
