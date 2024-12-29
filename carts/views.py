from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from carts.mixins import CartMixin
from carts.models import Cart
from django.template.loader import render_to_string
from goods.models import Products
from carts.utils import get_user_carts


class CartAddView(CartMixin, View):
    def post(self, request):
        product_id = request.POST.get("product_id")
        product = Products.objects.get(id=product_id)

        cart = self.get_cart(request, product=product)

        if cart:
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(user=request.user if request.user.is_authenticated else None,
                                session_key=request.session.session_key if not request.user.is_authenticated else None,
                                product=product, quantity=1)
        
        response_data = {
            "message": "Товар добавлен в корзину",
            'cart_items_html': self.render_cart(request)
        }

        return JsonResponse(response_data)


class CartChangeView(CartMixin, View):
    def post(self, request):
        cart_id = request.POST.get("cart_id")
        
        cart = self.get_cart(request, cart_id=cart_id)

        cart.quantity = request.POST.get("quantity")
        cart.save()

        updated_quantity = cart.quantity

        user_cart = get_user_carts(request)
        context = {"carts": user_cart}

        referer = request.META.get('HTTP_REFERER')
        if reverse('orders:create_order') in referer:
            context["order"] = True

        cart_items_html = render_to_string(
            "carts/includes/included_cart.html", context, request=request
        )

        responce_data = {
            'message': 'Количество товара изменено',
            'cart_items_html': cart_items_html,
            'updated_quantity': updated_quantity,
        }

        return JsonResponse(responce_data)

  
class CartRemoveView(CartMixin, View):
    def post(self, request):
        cart_id = request.POST.get("cart_id")
        
        cart = self.get_cart(request, cart_id=cart_id)
        quantity = cart.quantity
        cart.delete()

        response_data = {
            "message": "Товар удален из корзины",
            "quantity_deleted": quantity,
            'cart_items_html': self.render_cart(request)
        }

        return JsonResponse(response_data)

# def cart_add(request):
    
#     product_id = request.POST.get('product_id')
#     product = Products.objects.get(id=product_id)

#     if request.user.is_authenticated:
#         carts = Cart.objects.filter(user=request.user, product=product)

#         if carts.exists():
#             cart = carts.first()
#             cart.quantity += 1
#             cart.save()
#         else:
#             cart = Cart.objects.create(user=request.user, product=product, quantity=1)

#     else:
#         cart = Cart.objects.filter(session_key=request.session.session_key, product=product)

#         if cart.exists():
#             cart = cart.first()
#             cart.quantity += 1
#             cart.save()

#         else:
#             Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)
    
#     user_cart = get_user_carts(request)
#     cart_items_html = render_to_string(
#         'carts/includes/included_cart.html', {"carts": user_cart}, request=request
#         )
    
#     responce_data = {
#         'message': 'Товар добавлен в корзину',
#         'cart_items_html': cart_items_html,
#     }

#     return JsonResponse(responce_data)

# def cart_change(request):
#     cart_id = request.POST.get('cart_id')
#     quantity = request.POST.get('quantity')

#     cart = Cart.objects.get(id=cart_id)
#     cart.quantity = quantity
#     cart.save()
#     updated_quantity = cart.quantity

#     cart = get_user_carts(request)
#     cart_items_html = render_to_string(
#         'carts/includes/included_cart.html', {"carts": cart}, request=request
#         )
    
#     responce_data = {
#         'message': 'Количество товара изменено',
#         'cart_items_html': cart_items_html,
#         'updated_quantity': updated_quantity,
#     }

#     return JsonResponse(responce_data)

# def cart_remove(request):

#     cart_id = request.POST.get('cart_id')
    
#     cart = Cart.objects.get(id=cart_id)
#     quantity = cart.quantity
#     cart.delete()

#     user_cart = get_user_carts(request)
#     cart_items_html = render_to_string(
#         'carts/includes/included_cart.html', {"carts": user_cart}, request=request
#         )
    
#     responce_data = {
#         'message': 'Товар удален из корзины',
#         'cart_items_html': cart_items_html,
#         'quantity_deleted': quantity,
#     }

#     return JsonResponse(responce_data)

  

