from django.db import models

from .cart import Cart
from .product import Product


class CartItem(models.Model):
    class Meta:
        unique_together = ("cart", "product")
        db_table = "app_cart_items"

    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cart", null=False
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product", null=False
    )
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
