from django.shortcuts import render
from .models import Order, OrderItem , Product
from cart.models import Cart, CartItem
from django.contrib.auth.decorators import login_required




@login_required
def place_order(request):
    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.cartitem_set.all()

        shipping_address = request.POST.get('shipping_address')
        payment_method = request.POST.get('payment_method')

        order = Order.objects.create(user=request.user, shipping_address=shipping_address, payment_method=payment_method)

        for cart_item in cart_items:
            OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)

        cart_items.delete()

        return render(request, 'orders/order_confirmation.html', {'order': order})
    else:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.cartitem_set.all()
        total_price = cart.total_price_field
        return render(request, 'orders/place_order.html', {'cart_items': cart_items, 'total_price': total_price})



