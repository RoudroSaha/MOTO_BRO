from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def cars(request):
    return render(request, 'cars/cars.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')   

def contact(request):
    return render(request, 'pages/contact.html')    

def search(request):
    return render(request, 'cars/search.html')

