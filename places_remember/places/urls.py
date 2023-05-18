from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/login-success', views.login_success, name='login_success'),
    path('logout/', views.logout_view, name='logout'),
]
