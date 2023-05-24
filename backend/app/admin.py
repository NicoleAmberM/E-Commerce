from django.contrib import admin

from .models.cart import Cart
from .models.cart_item import CartItem
from .models.category import Category
from .models.order import Order
from .models.payment_method import PaymentMethod
from .models.product import Product
from .models.rating import Rating
from .models.role import Role
from .models.status import Status
from .models.user import User

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(PaymentMethod)
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Role)
admin.site.register(Status)
admin.site.register(User)
