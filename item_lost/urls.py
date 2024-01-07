from django.urls import path
from item_lost import views

urlpatterns=[
    path('',views.item_lost,name="lost"),
    path('found',views.item_found,name='found'),
]