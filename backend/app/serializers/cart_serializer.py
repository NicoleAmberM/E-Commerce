from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.serializers.datetime_serializer import DateTimeSerializer
from rest_framework import serializers


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ("product", "quantity", "subtotal")

    def get_product(self, obj):
        product = obj.product
        return {"name": product.name, "price": product.price}

    def get_subtotal(self, obj):
        return obj.product.price * obj.quantity


class CartSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    cart_items = serializers.SerializerMethodField()
    customer = serializers.SerializerMethodField()
    created_at = DateTimeSerializer(read_only=True)
    updated_at = DateTimeSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"

    def get_status(self, obj):
        return obj.status.name

    def get_customer(self, obj):
        customer = obj.customer
        return f"{customer.first_name} {customer.last_name}"

    def get_cart_items(self, obj):
        cart_items = CartItem.objects.filter(cart=obj)

        serialized_cart_items = CartItemSerializer(cart_items, many=True)
        return serialized_cart_items.data
