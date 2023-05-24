from app.views.product_view import ProductDetail, ProductList
from django.urls import path

urlpatterns = [
    path("products/", ProductList.as_view()),
    path("products/<slug:slug>", ProductDetail.as_view()),
]
