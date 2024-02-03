from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from item_found.models import *
from .models import Found

# Create your views here.




def aboutus(request):
    return render(request,'main/aboutus.html')

def contactus(request):
    return render(request,'main/contactus.html')

def form(request):
    if request.method =='POST':
        register = request.POST['register']
        student_name = request.POST['name']
        department = request.POST['dept']
        name = request.POST['item']
        category = request.POST['category']
        date = request.POST['date']
        location = request.POST['location']

        new_found=Found(register_number=register,student_name=student_name,department=department,item_name=name,item_category=category,found_date=date,location=location)
        new_found.save()
    return render(request,'main/foundForm.html')

def index(request):
    return render(request,'main/index.html')

def items(request):
    # found=products.object.all()
    # {'Register Number':id,'Item':found}
    return render(request,'main/items.html')

def login(request):
    return render(request,'main/login.html')

def register(request):
    # if request.method=='POST':
    #     register = request.POST['register']
    #     student_name = request.POST['name']
    #     department = request.POST['dept']
    #     name = request.POST['item']
    #     category = request.POST['category']
    #     date = request.POST['date']
    #     location = request.POST['location']

    #     new_found=Found(register_number=register,name=student_name,dept=department,item=name,category=category,found_date=date,location=location)
    #     new_found.save()
    return render(request,'main/register.html')

def products(request):
    # product=product.object.all()
    # student=register.object.all()
    # {'student':student,'product':product}
    return render(request,'found/products.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
    
        user.save()  
    
    return render(request,'main/login.html')




def found_dashboard(request):
    found_items = Found.objects.all()
    return render(request, 'main/found_dashboard.html', {'found_items': found_items})


