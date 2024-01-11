from django.urls import path
from item_found import views
#from .views import found

urlpatterns=[
    #path('found/', found, name='found'),
    path('form/',views.form,name='form'),
    path('found/',views.found,name='found'),

]

