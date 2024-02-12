from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    sex = models.CharField(
        max_length=10,
        choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")],
    )
    year = models.CharField(
        max_length=10,
        choices=[
            ("first", "First"),
            ("second", "Second"),
            ("third", "Third"),
            ("fourth", "Fourth"),
        ],
    )
    branch = models.CharField(
        max_length=100,
        choices=[
            ("ba", "BA"),
            ("bba", "BBA"),
            ("bsds", "BSC Data Science"),
            ("bsea", "BSC Economic Analytic"),
            ("msds", "MSC Data Science"),
            ("mba", "MBA"),
        ],
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class LostItem(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    item_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    description = models.TextField()
    reward = models.CharField(max_length=100, blank=True)
    item_image = models.ImageField(upload_to="lost_item_images/", blank=True, null=True)

    def __str__(self):
        return self.item_name



class LostItem(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    item_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    description = models.TextField()
    reward = models.CharField(max_length=100, blank=True)
    item_image = models.ImageField(upload_to="lost_item_images/", blank=True, null=True)

    def __str__(self):
        return self.item_name


class FoundItem(models.Model):
    finder = models.ForeignKey(User, on_delete=models.CASCADE)
    lost_item = models.ForeignKey("LostItem", on_delete=models.CASCADE)
    found_location = models.CharField(max_length=100)
    found_date = models.DateField()
    description = models.TextField()
    item_image = models.ImageField(
        upload_to="found_item_images/", blank=True, null=True
    )

    def __str__(self):
        return f"Found: {self.lost_item.item_name} by {self.finder.email}"


class LostItemCount(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    count=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} ({self.category}):{self.count}"

class FoundItemCount(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.CharField(max_length=50)
    count=models.IntegerField(default=0)