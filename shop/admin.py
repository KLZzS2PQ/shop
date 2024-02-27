from django.contrib import admin

from django.contrib import admin
from .models import Product, Order, Rarity


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity', 'image', 'desc', 'price', )
    list_editable = ('rarity', 'image', 'desc', 'price',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'delivery_address', 'created_at',)
    list_editable = ('delivery_address',)


@admin.register(Rarity)
class RarityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', )
    list_editable = ('name', 'color', )