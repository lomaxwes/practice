
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, login
from .models import Place, User, UserProfile
from .forms import MemoryForm
from django.conf import settings


# Create your views here.
def default_map(request):
    mapbox_access_token = settings.MAPBOX_ACCESS_TOKEN
    return render(request, 'places/map.html', {'mapbox_access_token': mapbox_access_token})


def home(request):
    # Preparing data for transmission to the template
    user = request.user
    firstname = user.first_name if user.is_authenticated else None
    if firstname or user.username:
        memories = Place.objects.filter(user=user)
        return render(request, 'places/home.html', {'firstname': firstname, 'memories': memories})
    else:
        return render(request, 'places/home.html', {'firstname': firstname})


@login_required
def login_success(request):
    # Preparing data for transmission to the template
    user = request.user
    firstname = user.first_name if user.is_authenticated else None
    return render(request, 'account/login_success.html', {'firstname': firstname})


def logout_view(request):
    # User logout
    logout(request)
    return redirect('home')


@login_required
def add_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.user = request.user  # Assign the current user to the user field
            place.save()
            return redirect('home')
    else:
        form = MemoryForm()

    return render(request, 'places/add_memory.html', {'form': form})


def memory_list(request):
    # Preparing data for list of memories
    memories = Place.objects.filter(user=request.user)
    return render(request, 'memory_list.html', {'memories': memories})


@login_required
def profile(request):
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = None

    context = {'user': user, 'profile': profile}
    return render(request, 'profile.html', context)
