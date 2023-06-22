from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.product import Product
from app.permissions import IsCustomer
from app.serializers.cart_serializer import CartSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class AddToCartView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        # check if user has a cart
        try:
            cart = Cart.objects.get(customer=user, status=1)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(customer=user)

        product_id = request.data.get("id")
        product_qty = request.data.get("quantity")

        # check if product exists
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # check if product qty is valid
        if product_qty <= 0:
            return Response(
                {"error": "Invalid product quantity"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if product_qty > product.stock:
            return Response(
                {"error": "Insufficient product stocks"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # check if product is already in the cart
        try:
            cart_item = CartItem.objects.get(product=product_id, cart=cart)
            cart_item.quantity += product_qty
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                cart=cart, product=product, quantity=product_qty
            )

        # update cart and products
        product.stock -= product_qty
        product.save()

        cart.item_count += product_qty
        cart.subtotal += cart_item.product.price * product_qty
        cart.save()

        serialized_data = self.serializer_class(cart)

        return Response(
            {"message": "Successfully added to cart", "data": serialized_data.data},
            status=status.HTTP_201_CREATED,
        )


class CartDetail(generics.RetrieveUpdateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "customer_id"

    def get_queryset(self):
        customer_id = self.kwargs["customer_id"]
        return Cart.objects.filter(customer_id=customer_id, status=1)

    def update(self, request, *args, **kwargs):
        cart = self.get_object()

        product_id = request.data.get("id")
        product_qty = request.data.get("quantity")

        try:
            product = Product.objects.get(pk=product_id)
            cart_item = CartItem.objects.get(product=product_id, cart=cart)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # check updated quantity
        # if cart item qty = 0, delete cart item
        # req qty can be a negative value, but the cart item qty should not be negative
        if (cart_item.quantity + product_qty) < 0:
            return Response(
                {"error": "Invalid product quantity"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if (cart_item.quantity + product_qty) == 0:
            cart.item_count -= cart_item.quantity
            cart.subtotal -= cart_item.product.price + cart_item.quantity
            cart.save()

            product.stock += cart_item.quantity
            product.save()

            cart_item.delete()

        else:
            if product_qty > product.stock:
                return Response(
                    {"error": "Insufficient product stocks"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            cart_item.quantity += product_qty
            cart_item.save()

            product.stock -= product_qty
            product.save()

            cart.item_count += product_qty
            cart.subtotal += cart_item.product.price * product_qty
            cart.save()

        serialized_data = self.serializer_class(cart)

        return Response(
            {"message": "Updated cart", "data": serialized_data.data},
            status=status.HTTP_200_OK,
        )
