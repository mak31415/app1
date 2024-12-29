from django.urls import path

from users.views import UserLoginView, logout, UserProfileView, UserRegistrationView, UserCartView

app_name = "users"

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'), 
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('users-cart/', UserCartView.as_view(), name='users_cart'),
    path('logout/', logout, name='logout'),
]
