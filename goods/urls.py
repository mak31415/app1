from django.urls import path

from goods.views import catalog, product 

app_name = "goods"

urlpatterns = [
    path('search/', catalog, name='search'),
    path('<slug:category_slug>', catalog, name='index'), 
    # path('<slug:category_slug>/<int:page>/', catalog, name='index'), 
    # path('product/', product, name='product'), # Перенаправление на страницу с каталогом
    # path('product/<int:product_id>/', product, name='product'),
    path('product/<slug:product_slug>/', product, name='product'),
]
