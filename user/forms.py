from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    poderes = forms.CharField(max_length=50)
    estado = forms.CharField(max_length=50)
    cidade = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'poderes', 'estado', 'cidade', 'password1', 'password2']