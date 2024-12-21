from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from goods.models import Products

def catalog(request):

  goods = Products.objects.all()

  context = {
    'title': 'Home - Каталог',
    'goods': goods,
  }
  return render(request, 'goods/catalog.html', context)

def product(request, product_id=None, product_slug=None):

  if product_id:
    product = get_object_or_404(Products, id=product_id)
  elif product_slug:
    product = get_object_or_404(Products, slug=product_slug)
  else:
    return HttpResponse('Product not found')
    
  context = {
    'product': product,
  }

  return render(request, 'goods/product.html', context=context)
