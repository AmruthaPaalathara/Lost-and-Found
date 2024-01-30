from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def lostForm(request):
    if request.method =='POST':
        register=request.POST['register']
        # name=

    return render(request,'main/lostForm.html')

def login_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    
    return render(request,'Login/login.html')
