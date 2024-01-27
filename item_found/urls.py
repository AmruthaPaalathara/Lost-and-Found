from django.urls import path
from  . import views
#from .views import found

urlpatterns=[
<<<<<<< HEAD
    path('form',views.foundForm,name='foundForm'),
    #path('',views.found,name='found'),
    path('login',views.login,name="login"),
    #path('log_form',views.login_form,name="login_form"),
    path('items',views.items,name='items'),
=======
    path('form',views.form,name='form'),
    path('',views.found,name='found'),
    #path('login',views.login,name="login"),
    path('log_form',views.login_form,name="login_form"),
>>>>>>> d6125521eeadf5ab54bd88530ce044a24e683666

]
