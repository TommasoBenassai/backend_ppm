from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import Cart, CartItem, Product



@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    cart_item = CartItem.objects.filter(cart=cart, product=product).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = CartItem.objects.create(cart=cart, product=product, quantity=1)

    cart.update_total_price()

    return redirect('view_cart')






def view_cart(request):
    user = request.user

    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            cart = None
        context = {'cart': cart}
        return render(request, 'cart/view_cart.html', context)
    else:
        return redirect('login')


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('view_cart')


@login_required
def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.quantity += 1
    item.save()

    cart = Cart.objects.get(user=request.user)
    cart.update_total_price()


    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    cart = Cart.objects.get(user=request.user)
    cart.update_total_price()

    return redirect('view_cart')





