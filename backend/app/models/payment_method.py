from django.db import models


class PaymentMethod(models.Model):
    class Meta:
        db_table = "app_payment_methods"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
