from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  

# Create your views here.
def home(request):
    
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def data(request):
    return render(request, 'data.html')

def home1(request):
    return render(request, 'home1.html')

def login_user(request):

    return render(request, 'login.html')

def signup_user(request):
    return render(request, 'signup.html')

def logout_user(request):
    pass

