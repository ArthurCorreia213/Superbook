from django.shortcuts import render, redirect
from django.views.generic import CreateView
from blog.models import Post
from django.urls import reverse_lazy
from .models import Comentario

# Create your views here.

class CriarPost(CreateView):
    model = Comentario
    template_name = 'blog/criar_post.html'
    fields = ['texto']
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        super().form_valid(form)
        return redirect('posts')