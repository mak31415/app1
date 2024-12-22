from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.core.paginator import Paginator
from django.http import HttpResponse
from goods.models import Products

def catalog(request, category_slug, page=1):

  if category_slug == 'all':
    goods = Products.objects.all()
  else:
    goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

  paginator = Paginator(goods, 3)
  current_page = paginator.page(page)

  context = {
    'title': 'Home - Каталог',
    'goods': current_page,
    'slug_url': category_slug,
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

