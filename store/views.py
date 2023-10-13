from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Category, Product


def categories(request):
    return {
        "categories": Category.objects.all(),
    }


def index(request):
    all_products = Product.objects.all()

    return render(
        request,
        "store/index.html",
        {
            "products": all_products,
        },
    )


def products(request):
    all_products = Product.objects.all()

    return render(
        request,
        "store/products.html",
        {
            "products": all_products,
        },
    )


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)

    return render(
        request,
        "store/category.html",
        {"category": category, "products": products},
    )


def product(request, slug):
    product = get_object_or_404(Product, slug=slug, published=True)

    return render(
        request,
        "store/product.html",
        {
            "product": product,
        },
    )
