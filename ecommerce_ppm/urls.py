from django.contrib import admin
from django.urls import path, include
from authentication.views import user_login, user_signup
from products import views as product_views
from cart import views as cart_views
from orders import views as order_views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from authentication.views import user_signup
from authentication.views import user_signup, user_login, user_logout
from django.conf import settings
from django.conf.urls.static import static
from products import views





urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('cart/remove/<int:item_id>/', cart_views.remove_from_cart, name='remove_from_cart'),
    path('products/', product_views.product_list, name='product_list'),
    path('products/<int:product_id>/', product_views.product_detail, name='product_detail'),
    path('products/categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('products/add_to_cart/<int:product_id>/', cart_views.add_to_cart, name='add_to_cart'),
    path('cart/', cart_views.view_cart, name='view_cart'),
    path('place_order/', order_views.place_order, name='place_order'),
    path('admin/', admin.site.urls),
    path('cart/increase_quantity/<int:item_id>/', cart_views.increase_quantity, name='increase_quantity'),
    path('search-product/', views.search_product, name='search_product'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
