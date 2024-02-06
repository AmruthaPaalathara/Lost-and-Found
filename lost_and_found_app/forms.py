from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, LostItem, FoundItem


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "full_name",
            "email",
            "phone_number",
            "sex",
            "year",
            "branch",
            "password1",  # Use 'password1' for the password field
        ]
        widgets = {
            "password1": forms.PasswordInput(),  # Render the password input type
        }


class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = [
            "name",
            "email",
            "item_name",
            "item_image",
            "location",
            "date",
            "description",
            "reward",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "item_name": forms.TextInput(attrs={"class": "form-control"}),
            "item_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "reward": forms.NumberInput(attrs={"class": "form-control"}),
        }



class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = [
            "lost_item",
            "found_location",
            "found_date",
            "description",
            "item_image",
        ]
        widgets = {
            "lost_item": forms.Select(attrs={"class": "form-control", "required" : False}),
            "found_location": forms.TextInput(attrs={"class": "form-control"}),
            "found_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "item_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

