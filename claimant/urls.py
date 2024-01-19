from django.urls import path
from . import views

urlpatterns=[

    path('',views.login_form,name="login_form"),
    #path('',views.claimant,name="claimant"),
    path('form',views.claimant_form,name="form"),

]