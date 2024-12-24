from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
  
  class Meta:
        model = User
        fields = ['username', 'password']

  username = forms.CharField()
  password = forms.CharField()