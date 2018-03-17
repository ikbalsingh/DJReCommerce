from django.contrib import admin
from .models import Buyer, Wishlist, Cart, Order, Forum, Rating

# Register your models here.
admin.site.register(Buyer)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Forum)
admin.site.register(Rating)
