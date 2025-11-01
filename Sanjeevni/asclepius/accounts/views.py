from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Profile

# app_name/views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from geopy.geocoders import Nominatim

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            profile= Profile.objects.create(user=user)
            add = form.cleaned_data.get('add')
            print(add)
            try:
                geolocator = Nominatim(user_agent="myapp")
                location = geolocator.geocode(add)
                print(location)
                if location:
                    profile.latitude = location.latitude
                    profile.longitude = location.longitude
                    profile.save()
                    print(profile.latitude)
                    print('done')
            except Exception as e:
                print(f"Geocoding failed: {e}")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
