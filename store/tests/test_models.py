from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Product, Category


class CategoryModelTest(TestCase):
    def test_category_model_exists(self):
        categories = Category.objects.all()

        self.assertEqual(categories.count(), 0)

    def test_category_is_valid(self):
        category = Category.objects.create(name="Test category", slug="test-category")
        self.assertEqual(str(category), "Test category")
        self.assertTrue(isinstance(category, Category))


class ProductModelTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username="admin")
        self.category = Category.objects.create(
            name="Test category", slug="test-category"
        )

        self.product = Product.objects.create(
            category=self.category,
            created_by=self.user,
            title="Product 1",
            description="Product description",
            slug="product-1",
            quantity=25,
            min_stock_level=5,
            price=2500.00,
            weight_in_kgs=2,
            is_bottle=True,
        )

    def test_product_model_exists(self):
        products = Product.objects.all()
        self.assertEqual(products.count(), 1)

    def test_product_is_valid(self):
        self.assertTrue(isinstance(self.product, Product))
        self.assertTrue(str(self.product), "Product 1")
