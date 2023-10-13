from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("store:category", args=[self.slug])

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.PROTECT
    )
    created_by = models.ForeignKey(
        User, related_name="product_creator", on_delete=models.PROTECT
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    quantity = models.IntegerField(default=0)
    min_stock_level = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    weight_in_kgs = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    weight_in_grams = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )

    volume_in_millilitres = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    volume_in_litres = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    volume_in_centilitres = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )

    is_pack = models.BooleanField(blank=True, null=True)
    is_pouch = models.BooleanField(blank=True, null=True)
    is_bottle = models.BooleanField(blank=True, null=True)
    is_container = models.BooleanField(blank=True, null=True)

    published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to="images/", null=True, blank=True)

    class Meta:
        verbose_name_plural = "products"
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.title} ({self.size}{self.size_unit})"

    def get_absolute_url(self):
        return reverse("store:product", args=[self.slug])

    @property
    def size(self):
        if self.weight_in_grams:
            return self.weight_in_grams
        if self.weight_in_kgs:
            return self.weight_in_kgs
        if self.volume_in_litres:
            return self.volume_in_litres
        if self.volume_in_millilitres:
            return self.volume_in_millilitres
        if self.volume_in_centilitres:
            return self.volume_in_centilitres

    @property
    def size_unit(self):
        if self.weight_in_grams:
            return "g"
        if self.weight_in_kgs:
            return "kg"
        if self.volume_in_litres:
            return "l"
        if self.volume_in_millilitres:
            return "ml"
        if self.volume_in_centilitres:
            return "cl"
