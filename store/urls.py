from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path("", views.index, name="index"),
    path("search/<slug:category_slug>", views.category, name="category"),
    path("category/<slug:category_slug>", views.category, name="category"),
    path("products/<slug:slug>", views.product, name="product"),
    path("products/", views.products, name="products"),
]
