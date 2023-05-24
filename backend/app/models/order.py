from django.db import models

from .cart import Cart
from .payment_method import PaymentMethod
from .status import Status


class Order(models.Model):
    class Meta:
        db_table = "app_orders"

    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="order", null=False
    )
    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.CASCADE,
        related_name="payment_method",
        null=False,
    )
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="order_status", null=False
    )
    total = models.DecimalField(max_digits=8, decimal_places=2)
    is_for_delivery = models.BooleanField(default=True)
    delivery_fee = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    estimated_completion_date = models.DateField(null=False)
    estimated_completion_time = models.TimeField(null=False)
    notes = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
