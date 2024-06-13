from django.contrib import admin
from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'item_count')

    def item_count(self, obj):
        return obj.items.count()

    item_count.short_description = 'Numero di elementi nel carrello'

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)


