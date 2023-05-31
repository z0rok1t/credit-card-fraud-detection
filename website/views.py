from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  
from django.contrib.auth.models import User
#from .forms import SignUpForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def data(request):
    return render(request, 'data.html')

def home1(request):
    return render(request, 'home1.html')

def login_user(request):

    if request.method == 'POST':
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

# def signup_user(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             #Authenticate and log in
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(uaername=username, password=password)
#             login(request, user)
#             messages.success(request, "You have successfully registred!")
#             return redirect('home')
#     else:
#         form = SignUpForm()
#         return render(request, 'signup.html', {'form': form})
#     return render(request, 'signup.html', {'form': form})

def signup_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return HttpResponse("Enter the same password!!")
        else:
            user = User.objects.create_user(username, email, password1)
            user.save()
            return redirect('login')
 
    return render(request, 'signup.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

