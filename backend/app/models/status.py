from django.db import models


class Status(models.Model):
    class Meta:
        verbose_name_plural = "Status"
        db_table = "app_status"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
