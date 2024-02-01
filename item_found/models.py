from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Found(models.Model):
    register_number = models.ForeignKey(User,blank=True, null=True,on_delete=models.SET_NULL)
    student_name = models.CharField(max_length=25)
    department = models.CharField(max_length=25)
    item_name = models.CharField(max_length=50)
    item_category = models.CharField(max_length=50)
    found_date = models.DateField(null=True, blank=True)
    location = models.TextField()
    image = models.ImageField(upload_to='media',null=True)

    def __str__(self):
        return str(self.register_number)
