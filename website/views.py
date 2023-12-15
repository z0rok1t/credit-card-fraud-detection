from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  
from django.contrib.auth.models import User
from .helpers import train_model, predicting
from .models import datasettt
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def data(request):
    return render(request, 'data.html')



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
            messages.success(request, "Passwords do NOT match, Try Again!!")
        else:
            user = User.objects.create_user(username, email, password1)
            user.save()
            return redirect('login')
 
    return render(request, 'signup.html')


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')



@login_required
def upload_dataset(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_data = request.FILES['file']
            #file2=request.FILES['file']
            train_model(file_data)
            #ataset=datasettt.objects.all()
            #ataset.delete()
            #lines = file2.read().decode().splitlines()
            #k=0
            #for line in lines[1:]:
            #    if k>100:
            #        print("breaked")
            #        break
            #    else:
            #        fields= line.split(',')
            #        field_data = { 'Time' : fields[0]}
            #        for j in range(1,29):
            #            field_name=f'V{j}'
            #            field_data[field_name]= float(fields[j])
            #        field_data["Amount"]=float(fields[29])
            #        field_data["Class"]=fields[30]
            #        print(f"row{j}")
            #        dataset = datasettt.objects.create(**field_data) 
            #        k+=1
            print("trained") 
            return redirect('/prediction')
    else:
        form = UploadFileForm()
    return render(request, 'home1.html', {'form': form})


def data(request):
    dataset=datasettt.objects.all()
    return render(request, 'data.html', {'dataset': dataset})

@login_required
def prediction(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_data = request.FILES['file']
            predictions = predicting(file_data)
            return render(request, 'results.html', {'predictions': predictions})
    else:
        form = UploadFileForm()
    return render(request, 'prediction.html', {'form': form})

def results(request):
    return render(request, 'results.html')