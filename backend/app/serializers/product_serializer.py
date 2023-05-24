from app.models.category import Category
from app.models.product import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_category(self, obj):
        category = Category.objects.get(pk=obj.category_id)
        return {"name": category.name, "slug": category.slug}
