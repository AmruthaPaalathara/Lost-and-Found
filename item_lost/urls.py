from django.urls import path
from item_lost import views
from .views import *

urlpatterns=[
    path("form",lostForm,name="lostForm"),
    # path('login',views.login,name='login'),
    # path('logout',views.logout,name="logout"),
    #path('log_form',views.login_form,name="login_form"),
    path('lost_dashboard', views.lost_dashboard, name ='lost_dashboard'),
    

]