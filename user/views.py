from django.shortcuts import render

from .forms import UserRegisterForm

from django.views.generic import ListView

from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            print(f"Conta criada para user {username}")
            print(f'\n\n\n\n\n\n\n{form}\n\n\n\n\n\'')
        else:
            print("FORMULARIO INVALIDO")
            print(form)
            print(form.errors)
            print(form.error_messages)
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

class ListarHerois(ListView):
    model = User
    template_name = 'user/users.html'
    context_object_name = 'herois'

    def get_queryset(self):
        return User.objects.all()