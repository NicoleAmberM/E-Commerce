from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.product import Product
from app.models.user import User
from app.serializers.cart_serializer import CartSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class AddToCartView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        # check if user is authenticated
        # user = request.user
        # if not user:
        #   return Response({"error": "Unauthenticated"}, status=status.HTTP_403_FORBIDDEN)

        # check if user is a customer (role)

        # temporary user
        user = User.objects.get(pk=1)

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
