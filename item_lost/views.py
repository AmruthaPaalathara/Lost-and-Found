from django.shortcuts import render
<<<<<<< HEAD
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.


=======
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def item_lost(request):
    return render(request,'')

def home(request):
    return render(request, 'homepage.html')
>>>>>>> d6125521eeadf5ab54bd88530ce044a24e683666

def login_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
<<<<<<< HEAD
        
        user=authenticate(request,username=username,password=password)
    return render(request,'login/login.html')

def lostForm(request):
    return render(request,'main/lostForm.html')

def login(request):
    return render(request,'main/login.html')

def index(request):
    return render(request,'main/index.html')
=======

    user = authenticate(request, username=username, password=password)
    
    return render(request,'Login/login.html')
>>>>>>> d6125521eeadf5ab54bd88530ce044a24e683666
