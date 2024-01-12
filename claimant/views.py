from django.shortcuts import render

# Create your views here.
def claimant(request):
    return render(request,'claimant/claimant-home.html')

def claimant_form(request):
    return render(request,'found/claimant-form.html')