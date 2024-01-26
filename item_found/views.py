from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from . models import found

# Create your views here.



def found(request):
    return render(request,'found/found.html')

def form(request):
    return render(request,'found/claim_form.html')


def login_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
    
        user.save()  
    
    return render(request,'Login/login.html')

#def edit(request):
    #return render(request)