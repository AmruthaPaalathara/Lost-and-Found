from django.urls import path
from item_lost import views

urlpatterns=[
    path('',views.item_lost,name="lost"),
    path('found',views.item_found,name='found')
<<<<<<< HEAD

=======
>>>>>>> 33ef6e31090ab36ac63016eb1ecc7e1ee43fd1b6
]