from unittest import skip

from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User

from store.models import Category, Product


# @skip("Demonstrating skipping tests")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass


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
        reverse_response = self.client.get(
            reverse("store:product_detail", args=["product-1"])
        )

        self.assertEqual(absolute_url, "/product-1")

        self.assertContains(response, "Product 1")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/products/product.html")

        self.assertContains(reverse_response, "Product 1")
        self.assertEqual(reverse_response.status_code, 200)
        self.assertTemplateUsed(reverse_response, "store/products/product.html")

    def test_category_absolute_url(self):
        absolute_url = self.category.get_absolute_url()
        response = self.client.get(absolute_url)
        reverse_response = self.client.get(
            reverse("store:category_detail", args=["test-category"])
        )

        self.assertEqual(absolute_url, "/shop/test-category")

        self.assertContains(response, "Product 1")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/categories/category.html")

        self.assertContains(reverse_response, "Test Category")
        self.assertEqual(reverse_response.status_code, 200)
        self.assertTemplateUsed(reverse_response, "store/categories/category.html")

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.client.get("/", HTTP_HOST="noaddress.com")
        self.assertEqual(response.status_code, 400)

        response = self.client.get("/", HTTP_HOST="yourdomain.com")
        self.assertEqual(response.status_code, 200)
