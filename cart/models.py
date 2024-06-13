from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')
    total_price_field = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)

    def __str__(self):
        if self.user:
            return f"Carrello di {self.user.username}"
        return "Carrello anonimo"

    def total_price(self):
        cart_items = self.cartitem_set.all()
        total = 0
        for item in cart_items:
            price = item.product.price
            quantity = item.quantity
            item_total = price * quantity
            total += item_total
        self.total_price_field = total
        self.save(update_fields=['total_price_field'])
        return total

    def update_total_price(self):
        total_price = self.total_price()
        self.total_price_field = total_price
        Cart.objects.filter(pk=self.pk).update(total_price_field=total_price)





class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def update_total_price(self):
        self.cart.update_total_price()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


