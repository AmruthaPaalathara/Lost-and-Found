from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.




def login_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
    return render(request,'login/login.html')

def lostForm(request):
    return render(request,'main/lostForm.html')

def login(request):
    return render(request,'main/login.html')

def index(request):
    return render(request,'main/index.html')