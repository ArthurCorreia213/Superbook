from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from .models import Post
from django.contrib.auth.models import User

# Create your views here.

class CriarPost(CreateView):
    model = Post
    template_name = 'blog/criar_post.html'
    fields = ['titulo', 'texto']

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
