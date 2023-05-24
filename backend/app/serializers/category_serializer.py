from app.models.category import Category
from app.models.product import Product
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    def get_products(self, obj):
        products = Product.objects.get(category_id=obj.id)
        return [
            {
                "id": product.product.id,
                "name": product.product.name,
                "slug": product.product.slug,
                "description": product.product.description,
                "price": product.product.price,
            }
            for product in products
        ]
