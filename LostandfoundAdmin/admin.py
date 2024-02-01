from django.contrib import admin
from .models import Claimant
#from .models import LostItem, FoundItem, UserProfile, StaffAction

# Register your models here.

@admin.register(Claimant)
class ClaimantAdmin(admin.ModelAdmin): #we are going inside the found admin.
    list_display = ('register_number','department','item_name','item_category')  #what all should be there in the front table table of found retrieved from model.
    ordering = ('item_name',)  #what should be the order of the list. Here we ae listing according to category.
    search_fields = ('register_number','item_name') #what all things we can search based on that one particular item.