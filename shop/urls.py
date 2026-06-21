from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'manufacturers', views.ManufacturerViewSet)
router.register(r'carts', views.CartViewSet)
router.register(r'cart-items', views.CartItemViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('about-shop/', views.about_shop, name='about_shop'),
    path('about-author/', views.about_author, name='about_author'),
    path('catalog/', views.product_list, name='product_list'),
    path('catalog/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    
    # Регистрация
    path('register/', views.register, name='register'),
    
    # Личный кабинет
    path('profile/', views.profile_page, name='profile_page'),
    path('api/me/', views.me_api, name='me_api'),
    path('api/orders/', views.my_orders_api, name='my_orders_api'),
]

urlpatterns += router.urls