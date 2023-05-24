from django.core.validators import MaxValueValidator
from django.db import models

from .product import Product
from .user import User


class Rating(models.Model):
    class Meta:
        db_table = "app_ratings"

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="ratings", null=False
    )
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ratings", null=False
    )
    score = models.IntegerField(null=False, validators=[MaxValueValidator(5)])
    review = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
