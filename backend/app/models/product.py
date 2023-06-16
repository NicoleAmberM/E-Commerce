from django.core.validators import MinLengthValidator
from django.db import models

from .category import Category


class Product(models.Model):
    class Meta:
        db_table = "app_products"

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products", null=False
    )
    name = models.CharField(
        max_length=255, unique=True, validators=[MinLengthValidator(3)]
    )
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=255, validators=[MinLengthValidator(12)])
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
