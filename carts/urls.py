from django.urls import path

from carts.views import cart_add, cart_change, cart_remove

app_name = 'carts'

urlpatterns = [
    path('cart_add/', cart_add, name='cart_add'),
    path('cart_change/', cart_change, name='cart_change'),
    path('cart_remove/', cart_remove, name='cart_remove'),
]