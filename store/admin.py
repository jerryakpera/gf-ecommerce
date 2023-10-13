from django.contrib import admin


from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "price",
        "quantity",
        "published",
        "created_at",
        "updated_at",
    ]
    list_filter = ["published", "price"]
    list_editable = ["price", "quantity"]
    prepopulated_fields = {"slug": ("title",)}
