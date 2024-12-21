from django.urls import path

from goods.views import catalog, product 

app_name = "goods"

urlpatterns = [
    path('<slug:category_slug>', catalog, name='index'), 
    #path('product/', product, name='product'),
    path('product/<int:product_id>/', product, name='product'),
    path('product/<slug:product_slug>/', product, name='product'),
]
