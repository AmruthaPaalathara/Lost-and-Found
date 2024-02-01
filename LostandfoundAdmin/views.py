from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout 
from django.contrib import messages


# Create your views here.


def claimant(request):
    if request.method=="POST":
        reg_no=request.POST['register_number']
        st_name=request.POST['name']
        dept=request.POST['dept']
        item_name=request.POST['item']
        item_category=request.POST['category']
        location=request.POST['location']
        date=request.POST['date']

        new_claim=claimant(register_number=reg_no,student_name=st_name,department=dept,item_name=item_name,item_category=item_category,lost_date=date,location=location)
        new_claim.save()
    return render(request,'main/claimantform.html')

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.success(request,('There was an Error Logging In, Try Again...'))
            return redirect('login')
    # else:
    #     pass
    #     return render(request,'authentication/login.html')