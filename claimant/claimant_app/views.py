from django.shortcuts import render

# Create your views here.
def claimant(request):
    return render(request,'claimant-home.html')

def claimant_home(request):
    return render(request,'claimant-form.html')