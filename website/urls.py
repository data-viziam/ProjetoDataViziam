from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # rota para a página inicial
    path('about/', views.sobre, name='about'),  # rota para a página sobre
    path('contact/', views.contato, name='contact'),  # rota para a página de contato
    path('login/', views.login, name='login'), # rota para a página de login
    path('new_user_form/', views.login, name='new_user_login'), # rota para a página de 'junte-se a nos'
]
