from app.views.auth_view import LoginView, LogoutView, RegisterView
from app.views.cart_view import AddToCartView, CartDetail
from app.views.product_view import ProductDetail, ProductList
from django.urls import path

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("products/", ProductList.as_view(), name="product-list"),
    path("products/<slug:slug>", ProductDetail.as_view(), name="product-detail"),
    path("cart/", AddToCartView.as_view(), name="add-to-cart"),
    path("cart/<int:customer_id>", CartDetail.as_view(), name="cart-detail"),
]
