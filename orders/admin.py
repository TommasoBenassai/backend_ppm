from django.contrib import admin
from orders.models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ['product', 'quantity']
    can_delete = False
    max_num = 0

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'shipping_address', 'payment_method', 'total_price']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
