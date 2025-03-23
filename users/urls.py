from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='users'), # rota para página de login
]
