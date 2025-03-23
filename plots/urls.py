from django.urls import path
from . import views

urlpatterns = [
    path('plots/', views.user_plots, name='user_plots'),
]