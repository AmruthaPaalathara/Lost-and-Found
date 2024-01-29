from django.urls import path
from  . import views
#from .views import found

urlpatterns=[
    path('about',views.aboutus,name='aboutus'),
    path('',views.index,name='index'),
    #path('login',views.login,name="login"),
    #path('log_form',views.login_form,name="login_form"),
    path('contact',views.contactus,name='contactus'),
    path('form',views.form,name='foundForm'),
    path('home',views.index,name='home'),
    path('item',views.items,name='items'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),

]
