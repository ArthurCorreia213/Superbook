from django.shortcuts import render

from .forms import UserRegisterForm

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})