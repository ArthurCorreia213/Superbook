"""
URL configuration for Superbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from user.views import register as user_register
from user.views import ListarHerois
from blog.views import ListarPosts, CriarPost

admin.site.site_header = "SuperBook Admin"
admin.site.site_title = "SuperBook Painel"
admin.site.index_title = "Bem-vindo ao SuperBook"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_register, name='register'),
    path('', ListarHerois.as_view(), name='herois'),
    path('posts/', ListarPosts.as_view(), name='posts'),
    path('posts/criar/', CriarPost.as_view(), name='criar_post'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path ('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]
