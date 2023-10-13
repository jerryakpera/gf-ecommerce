from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def index(request):
    all_products = Product.products.all()

    return render(
        request,
        "store/index.html",
        {
            "products": all_products,
        },
    )


def products_all(request):
    products = Product.products.all()

    return render(
        request,
        "store/products/products.html",
        {
            "products": products,
        },
    )


def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)

    return render(
        request,
        "store/categories/category.html",
        {"category": category, "products": products},
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, published=True)

    return render(
        request,
        "store/products/product.html",
        {
            "product": product,
        },
    )
