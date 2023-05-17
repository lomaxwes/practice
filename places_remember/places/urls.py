from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('login/google/', views.google_login, name='google_login'),
    path('login/vk/', views.vk_login, name='vk_login'),
]
