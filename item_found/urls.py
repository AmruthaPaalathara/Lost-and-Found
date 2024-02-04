from django.urls import path
from  . import views
from .views import found_dashboard

urlpatterns=[
    path('about',views.aboutus,name='aboutus'),
    path('index',views.index,name='index'),
    path('',views.login,name="login"),
    #path('log_form',views.login_form,name="login_form"),
    path('contact',views.contactus,name='contactus'),
    path('form',views.form,name='foundForm'),
    path('home',views.index,name='home'),
    path('item',views.items,name='items'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    #path('products',views.products,name='product'),
    path('found_dashboard/', views.found_dashboard, name='found_dashboard'),

]



