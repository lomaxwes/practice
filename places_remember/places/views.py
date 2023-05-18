from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from .models import User


# Create your views here.
def home(request):
    # Preparing data for transmission to the template
    user = request.user
    firstname = user.first_name if user.is_authenticated else None
    return render(request, 'places/home.html', {'firstname': firstname})


def login_success(request):
    # Preparing data for transmission to the template
    user = request.user
    firstname = user.first_name
    return render(request, 'account/login_success.html', {'firstname': firstname})


def logout_view(request):
    # User logout
    logout(request)
    return redirect('home')
