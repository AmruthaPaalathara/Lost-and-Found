from django.shortcuts import render

# Create your views here.
def item_lost(request):
    return render(request,'')

def index(request):
    return render(request, 'homepage.html')


def login_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        

    return render(request,'login/login.html')