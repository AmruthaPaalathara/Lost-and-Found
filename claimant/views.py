from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

# Create your views here.
def claimant(request):
    return render(request,'claimant/claimant-home.html')

def claimant_form(request):
    return render(request,'found/claimant-form.html')

def login_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        

    return render(request,'login/login.html')