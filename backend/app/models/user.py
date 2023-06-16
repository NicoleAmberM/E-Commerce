from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

from .role import Role


class User(AbstractUser):
    class Meta:
        app_label = "app"
        db_table = "app_users"

    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name="users", default=1
    )
    first_name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    email = models.EmailField(max_length=255, unique=True, null=False)
    contact_number = models.CharField(
        max_length=255, validators=[MinLengthValidator(12), MaxLengthValidator(12)]
    )
    address = models.CharField(max_length=255, validators=[MinLengthValidator(5)])
    street = models.CharField(max_length=255, validators=[MinLengthValidator(3)])
    city = models.CharField(max_length=255, validators=[MinLengthValidator(3)])
    is_active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return str(self.email)
