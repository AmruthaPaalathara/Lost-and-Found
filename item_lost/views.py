from django.shortcuts import render

# Create your views here.
def item_lost(request):
    return render(request,'claimant/claimant-home.html')
