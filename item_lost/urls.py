from django.urls import path
from item_lost import views

urlpatterns=[
<<<<<<< HEAD
    #path('losthome',views.item_lost,name="home"),
    path('lost',views.lostForm,name='lost'),
    #path('',views.index,name="index"),
    path('login',views.login,name='login'),
    path('',views.index,name='index')
=======
    path('losthome',views.item_lost,name="home"),
    path('lost',views.item_lost,name='lost'),
    path('',views.home,name="index"),
    path('log_form',views.login_form,name="login_form"),
>>>>>>> d6125521eeadf5ab54bd88530ce044a24e683666

]