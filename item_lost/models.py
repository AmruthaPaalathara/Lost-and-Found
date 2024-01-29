from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class lost(models.Model):
    register_number = models.IntegerField()
    student_name = models.CharField(max_length=25)
    department = models.CharField(max_length=25)
    item_lost = models.CharField(max_length=50)
    item_category = models.CharField(max_length=50)
    lost_date = models.DateField(null=True,blank=True)
    lost_place = models.TextField()

def __str__(self):
    return str(self.register_number)

class Status(models.Model):
    STATUS = (
    ('Pending','Pending'),
    ('Completed','Completed'),
)
    
    register_number=models.ForeignKey(lost,null=True,on_delete=models.CASCADE)
    status=models.CharField(max_length=10,null=True,choices=STATUS)