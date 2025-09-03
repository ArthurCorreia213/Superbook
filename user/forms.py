from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Heroi

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    poderes = forms.CharField(max_length=50)
    estado = forms.CharField(max_length=50)
    cidade = forms.CharField(max_length=50)

    class Meta:
        model = Heroi
        fields = ['username', 'email', 'poderes', 'estado', 'cidade', 'password1', 'password2']