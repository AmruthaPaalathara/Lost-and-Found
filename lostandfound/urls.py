"""
URL configuration for lostandfound project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from lostandfound import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('found/',include('item_found.urls')),
    #path("",login,name="login"),
    path("lost/",include("item_lost.urls")),
    path('',include('LostandfoundAdmin.urls')),
    # path('dadmin/',include('django.contrib.auth.urls')),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
