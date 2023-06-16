from app.views.auth_view import LoginView, LogoutView, RegisterView
from app.views.cart_view import AddToCartView
from app.views.product_view import ProductDetail, ProductList
from django.urls import path

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("products/", ProductList.as_view()),
    path("products/<slug:slug>", ProductDetail.as_view()),
    path("cart/", AddToCartView.as_view()),
]
