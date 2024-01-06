from django.urls import path
<<<<<<< HEAD
from item_lost import views

urlpatterns=[
    path('',views.item_lost,name="lost"),
=======
from item_found import views

urlpatterns=[
    path('found',views.item_found,name='found')
    
>>>>>>> 11c233bf5ed04b2dc4ad07dce094d7598984da13
]