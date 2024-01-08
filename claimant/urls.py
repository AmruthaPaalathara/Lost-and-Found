from django.urls import path
from claimant import views

urlpatterns=[
    path('',views.claimant,name="claimant"),
    path('form',views.claimant_form,name="form")
]