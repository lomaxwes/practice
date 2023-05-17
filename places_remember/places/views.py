from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'places/home.html')


def google_login(request):
    """
    google login page
    """
    return render(request, 'account/google_login.html')


def vk_login(request):
    pass
