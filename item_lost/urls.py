from django.urls import path
from item_lost import views
from item_lost.views import *


urlpatterns=[
    path('form',views.lostForm,name="lostForm"),
    #path('lost',views.item_lost,name='lost'),
    #path('',views.home,name="index"),
    #path('log_form',views.login_form,name="login_form"),
    path('lost_dashboard', lost_dashboard, name ='lost_dashboard'),
    

]