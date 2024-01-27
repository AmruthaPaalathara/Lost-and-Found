from django.shortcuts import render

# Create your views here.



# def login_form(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        

#     return render(request,'login/login.html')

def foundForm(request):
    return render(request,'main/foundForm.html')

def login(request):
    return render(request,'main/login.html')

def items(request):
    return render(request,'main/items.html')