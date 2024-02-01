
from django.urls import path
from .views import *

urlpatterns = [
    #path('login',login_form,name='padminlogin'),
    path('claim',claimant,name='claim'),
    path('',login_user,name='login')
]
