from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LostItemForm, FoundItemForm
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import LostItem, FoundItem


def index(request):
    # Your index view logic here
    return render(request, "lost_and_found/index.html")


def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            User = get_user_model()
            username = user.full_name + user.phone_number
            new_user = User.objects.create_user(
                # username=username,
                username=user.email,
                email=user.email,
                password=form.cleaned_data["password1"],
            )
            new_user.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "lost_and_found/Auth/register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")  # Assuming email is used for authentication
        password = request.POST.get("password")

        print("Email:", email)  # Debugging statement
        print("Password:", password)  # Debugging statement

        user = authenticate(request, username=email, password=password)
        if user is not None:
            print("User found:", user)  # Debugging statement
            login(request, user)
            # Redirect to a success page or homepage
            return redirect("index")
        else:
            # Authentication failed
            print("No user found")  # Debugging statement
            messages.error(request, "Invalid email or password. Please try again.")
            return redirect("login")  # Redirect to the login page with an error message
    else:
        return render(request, "lost_and_found/Auth/login.html")


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def report_lost_item(request):
    if request.method == "POST":
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                "index"
            )  # Redirect to the homepage after successful submission
        else:
            print("Form errors:", form.errors)
            # Optionally, you can return the form with errors to the template
            # return render(request, 'lost_and_found/lost.html', {'form': form})
    else:
        form = LostItemForm()
    return render(request, "lost_and_found/lost.html", {"form": form})


def aboutus(request):

    return render(request, "lost_and_found/info/aboutus.html")


@login_required(login_url="login")
def report_found_item(request):
    if request.method == "POST":
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            found_item = form.save(commit=False)
            found_item.finder_id = request.user.id
            found_item.save()
            return redirect("found_success")
    else:
        form = FoundItemForm()
    return render(request, "lost_and_found/found.html", {"form": form})


@login_required(login_url="login")
def found_success(request):
    return render(request, "lost_and_found/found_success.html")


def lost_item(request):
    lost_items = LostItem.objects.all()
    return render(request, "lost_and_found/lost_item.html", {"lost_items": lost_items})


def found_item(request):
    found_items = FoundItem.objects.all()
    return render(
        request, "lost_and_found/found_item.html", {"found_items": found_items}
    )
def contactus(request):
    return render(request,"lost_and_found\contactus.html")

