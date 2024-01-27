from django.urls import path
from item_lost import views

urlpatterns=[
    #path('losthome',views.item_lost,name="home"),
    path('lost',views.lostForm,name='lost'),
    #path('',views.index,name="index"),
    path('login',views.login,name='login'),
    path('',views.index,name='index')

]