from django.urls import path

from goods.views import CatalogView, ProductView

app_name = "goods"

urlpatterns = [
    path('search/', CatalogView.as_view(), name='search'),
    path('<slug:category_slug>', CatalogView.as_view(), name='index'), 
    # path('<slug:category_slug>/<int:page>/', catalog, name='index'), 
    # path('product/', product, name='product'), # Перенаправление на страницу с каталогом
    # path('product/<int:product_id>/', product, name='product'),
    path('product/<slug:product_slug>/', ProductView.as_view(), name='product'),
]
