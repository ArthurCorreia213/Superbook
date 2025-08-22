from django.shortcuts import render

from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            print(f"Conta criada para user {username}")
        else:
            print("FORMULARIO INVALIDO")
            print(form)
            print(form.errors)
            print(form.error_messages)
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})