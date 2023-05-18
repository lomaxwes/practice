from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # greeting
    path('account/login-success', views.login_success, name='login_success'),  # authentication
    path('logout/', views.logout_view, name='logout'),  # logout
]
