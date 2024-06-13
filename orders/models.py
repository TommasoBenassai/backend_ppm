from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    shipping_address = models.CharField(max_length=100, default='Indirizzo di default')
    PAYMENT_METHOD_CHOICES = [
        ('paypal', 'Paypal'),
        ('credit_card', 'Carta di credito'),
        ('bank_transfer', 'Bonifico bancario'),
    ]

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)


    def __str__(self):
        return f"Ordine {self.pk} di {self.user.username} ( {self.user.email} )"

    def total_price(self):
        total = 0
        for item in self.order_items.all():
            total += item.product.price * item.quantity
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} nell'ordine {self.order.pk}"
