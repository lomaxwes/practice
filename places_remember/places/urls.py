from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # greeting
    path('account/login-success', views.login_success, name='login_success'),  # user is authenticated
    path('logout/', views.logout_view, name='logout'),  # logout
    path('add_memory/', views.add_memory, name='add_memory'),  # add_memory
    path('map/', views.default_map, name='map')  # map
]
