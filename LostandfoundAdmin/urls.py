from django.urls import path
from LostandfoundAdmin import views


urlpatterns=[
    path('login',views.login_form,name='adminlogin')
]