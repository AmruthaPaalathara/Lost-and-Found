from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Claimant(models.Model):
    register_number = models.IntegerField(User,blank=True, null=True)
    student_name = models.CharField(max_length=25)
    department = models.CharField(max_length=25)
    item_name = models.CharField(max_length=50)
    item_category = models.CharField(max_length=50)
    lost_date = models.DateField(null=True, blank=True)
    location = models.TextField()

    def __str__(self):
        return str(self.register_number)

