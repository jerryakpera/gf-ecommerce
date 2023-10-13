from unittest import skip

from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User

from store.models import Category, Product


# @skip("Demonstrating skipping tests")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass


@skip("Demonstrating skipping tests")
class TestViews(TestCase):
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

    def test_index_returns_correct_response(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/index.html")
        self.assertContains(response, "Healthy foods and oils")

    def test_product_absolute_url(self):
        absolute_url = self.product.get_absolute_url()
        response = self.client.get(absolute_url)
        reverse_response = self.client.get(reverse("store:product", args=["product-1"]))

        self.assertEqual(absolute_url, "product/product-1/")

        self.assertContains(response, "Product 1")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/product.html")

        self.assertContains(reverse_response, "Product 1")
        self.assertEqual(reverse_response.status_code, 200)
        self.assertTemplateUsed(reverse_response, "store/product.html")

    def test_category_absolute_url(self):
        absolute_url = self.category.get_absolute_url()
        response = self.client.get(absolute_url)
        reverse_response = self.client.get(
            reverse("store:category", args=["test-category"])
        )

        self.assertEqual(absolute_url, "category/test-category/")

        self.assertContains(response, "Product 1")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/category.html")

        self.assertContains(reverse_response, "Test Category")
        self.assertEqual(reverse_response.status_code, 200)
        self.assertTemplateUsed(reverse_response, "store/category.html")
