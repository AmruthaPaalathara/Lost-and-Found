from django.contrib import admin
from .models import Found

# Register your models here.
#admin.site.register(Found)
#displaying those atttributes when we open the found section.
@admin.register(Found) #admin.ste.register(Found) is same as this.
class FoundAdmin(admin.ModelAdmin): #we are going inside the found admin.
    list_display = ('register_number','department','item_name','item_category','found_date')  #what all should be there in the front table table of found retrieved from model.
    ordering = ('item_name',)  #what should be the order of the list. Here we ae listing according to category.
    search_fields = ('register_number','item_name') #what all things we can search based on that one particular item.

    class FoundStaff(admin.ModelAdmin):
        list_display = ('register_number','department','item_name','image')
        list_filter = ('item_name','department')
        ordering = ('item_name')