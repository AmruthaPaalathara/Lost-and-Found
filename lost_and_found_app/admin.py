from django.contrib import admin
from .models import LostItem, FoundItem, User


admin.site.register(User)
admin.site.register(LostItem)
admin.site.register(FoundItem)
