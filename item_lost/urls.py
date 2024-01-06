from django.urls import path
from item_lost import views

urlpatterns=[
    path('',views.item_lost,name="lost"),
]