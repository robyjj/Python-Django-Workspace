from django.contrib import admin
from .models import Product, Offer


# if we don't register this , you wont be able to view th product details in admin screen
# You can only see ProductObject
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
