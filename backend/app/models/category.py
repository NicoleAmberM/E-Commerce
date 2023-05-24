from django.core.validators import MinLengthValidator
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
        db_table = "app_categories"

    name = models.CharField(
        max_length=255, unique=True, validators=[MinLengthValidator(3)]
    )
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
