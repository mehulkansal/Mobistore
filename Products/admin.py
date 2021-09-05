from django.contrib import admin
from Products.models import Product1, shop  # ,cart,  customer
# Register your models here.

admin.site.register(Product1)
# admin.site.register(cart)
admin.site.register(shop)
#
# admin.site.register(customer)
