from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

def index(request):
    context={'message':'Hello Braison'}
    return render(request,'index.html',context)

def Register(request):
    if request.user.is_authenticated:
         return redirect('home')
    else:
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid:
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Hello'+' '+ user+' '+'your account creation succesful')
            return redirect('login')

    context={'form':form}
    return render(request,'Register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
         return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,"Please check your password or username")
    context={}
    return render(request,'login.html',context)

def logUserOut(request):
    logout(request)
    return redirect('login') 

@login_required(login_url='login')
def home(request):
    context={}
    return render(request,'home.html',context)


# Dealing with maps api
from geopy.geocoders import Nominatim
from django.conf import settings

def map_view(request):
    # Example address to show
    address = "Nairobi, Kenya"
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(address)

    context = {
        'google_api_key': settings.google_API_KEY,  # Replace with your actual key
        'latitude': location.latitude,
        'longitude': location.longitude,
    }
    return render(request, 'map.html', context)