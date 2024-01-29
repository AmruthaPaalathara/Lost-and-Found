from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from item_found.models import *

# Create your views here.




def aboutus(request):
    return render(request,'main/aboutus.html')

def contactus(request):
    return render(request,'main/contactus.html')

def form(request):
    return render(request,'main/foundForm.html')

def index(request):
    return render(request,'main/index.html')

def items(request):
    return render(request,'main/items.html')

def login(request):
    return render(request,'main/login.html')

def register(request):
    return render(request,'main/register.html')


def login_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
    
        user.save()  
    
    return render(request,'Login/login.html')

#def edit(request):
    #return render(request)
