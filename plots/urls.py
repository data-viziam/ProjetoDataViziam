from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='plots'), # rota para página inicial dos gráficos
]
