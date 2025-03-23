from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # rota para a página inicial
    path('about/', views.about, name='about'),  # rota para a página sobre
    path('contact/', views.contact, name='contact'),  # rota para a página de contato
]
