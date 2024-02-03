from django.urls import path
from item_lost import views
from .views import lost_dashboard

urlpatterns=[
    path('form',views.lostForm,name="lostForm"),
    #path('lost',views.item_lost,name='lost'),
    #path('',views.home,name="index"),
    #path('log_form',views.login_form,name="login_form"),
    path('dashboard', views.lost_dashboard, name ='dashboard'),
    

]