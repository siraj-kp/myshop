from django.contrib import admin
from .models import Product, Offer, Order


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'phone', 'total', 'item_name')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)


