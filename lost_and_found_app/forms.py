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
            "date": forms.DateInput(attrs={"type": "date"}),
            "item_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
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
            "found_date": forms.DateInput(attrs={"type": "date"}),
            "item_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
