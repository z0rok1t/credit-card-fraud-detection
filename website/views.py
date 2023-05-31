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

    if request.method == "POST":
        #Check to see if logging in 
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #messages.success(request, "You have been logged in!")
            return redirect('home1')   #profile after its created
        else: 
            messages.success(request, "There was an error, Try again!")
            return redirect('login')
    else: 
        return render(request, 'login.html')

def signup_user(request):
    return render(request, 'signup.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

