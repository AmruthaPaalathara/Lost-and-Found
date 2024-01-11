from django.shortcuts import render

# Create your views here.



def found(request):
    return render(request,'found/found.html')

def login(request):
    return render(request,"login/login.html")