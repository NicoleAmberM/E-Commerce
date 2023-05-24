from django.db import models

from .status import Status
from .user import User


class Cart(models.Model):
    class Meta:
        db_table = "app_carts"

    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cart", null=False
    )
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="cart_status", default=1
    )
    item_count = models.IntegerField()
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
