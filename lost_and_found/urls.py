"""
URL configuration for lost_and_found project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from lost_and_found_app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("report-lost/", report_lost_item, name="report_lost_item"),
    path("aboutus/", aboutus, name="aboutus"),
    path("report-found/", report_found_item, name="report_found_item"),
    path("found-success/", found_success, name="found_success"),
    path("lost-item/", lost_item, name="lost_item"),
    path("found-item/", found_item, name="found_item"),
    path("contactus/", contactus, name="contactus"),
    path('admindashboard',admin_dashboard,name='admindashboard'),
    path('datatables',datatables,name='datatables'),
    path('admindashboard',admin_dashboard,name='dashboard'),
    path('datatables',datatables,name='datatables'),
    path("lostitems",lostitems,name="lostitems"),
    path("founditems",founditems,name="founditems"),
    path("lostcount",lost_item_users,name="lostusercount"),
    path("foundcount",found_item_users,name="foundusercount"),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
