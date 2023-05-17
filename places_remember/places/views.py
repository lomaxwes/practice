from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'places/home.html')


def google_login(request):
    pass


def vk_login(request):
    pass
