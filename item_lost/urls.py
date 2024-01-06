from django.urls import path
from item_found import views

urlpatterns=[
    path('found',views.item_found,name='found')
    
]