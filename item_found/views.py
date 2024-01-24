from django.shortcuts import render

# Create your views here.



def found(request):
    return render(request,'found/found.html')

def form(request):
    return render(request,'found/form_claim.html')

def login(request):
    return render(request,"Login/login.html")

def login_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        

    return render(request,'login/login.html')