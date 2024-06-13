from django.urls import path
from . import views
from . import add_to_cart

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/', views.product_list, name='product_list'),
    path('cart/', views.view_cart, name='view_cart'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('search-product/', views.search_product, name='search_product'),
]
