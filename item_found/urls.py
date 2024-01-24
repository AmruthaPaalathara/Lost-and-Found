from django.urls import path
from  item_found import views
#from .views import found

urlpatterns=[
    path('form',views.form,name='form'),
    path('',views.found,name='found'),
    path('login',views.login,name="login"),
    path('log_form',views.login_form,name="login_form"),

]
