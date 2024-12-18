from django.urls import path

from main.views import about, index

app_name = "main"

urlpatterns = [
    path('', index, name='index'), 
    path('about/', about, name='about')
]
