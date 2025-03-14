from django.db import models


class Role(models.Model):
    class Meta:
        db_table = "app_roles"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
