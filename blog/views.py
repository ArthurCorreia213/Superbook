from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormMixin
from .models import Post
from django.urls import reverse_lazy

from comments.forms import FormComentario

from django.contrib.auth import get_user_model
User=get_user_model()

from comments.models import Comentario

# Create your views here.

class CriarPost(CreateView):
    model = Post
    template_name = 'blog/criar_post.html'
    fields = ['titulo', 'texto']
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        super().form_valid(form)
        return redirect('posts')

class ListarPosts(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/posts.html'

    def get_queryset(self):
        return Post.objects.all()
    
class AtualizarPost(UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    fields = ['titulo', 'texto']
    success_url = reverse_lazy('posts')

class ApagarPost(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('posts')

class DetalhesPost(DetailView, FormMixin):
    model = Post
    template_name = 'blog/detail.html'
    form_class = FormComentario

    def get_context_data(self, **kwargs):
        post = super().get_context_data(**kwargs)
        comentarios = Comentario.objects.filter(post=post['post'].pk)
        print(comentarios)
        return {'post': post, 'comentarios':comentarios}
