from django.urls import path
from . import views
from cart import views


urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/increase_quantity/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
]