"""
URL configuration for my_project project.

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
from django.urls import path
from .import views
urlpatterns = [
  path("",views.user,name="user"),
  path("register",views.register,name="register"),
  path("registerview",views.registerview,name="registerview"),
  path("login",views.Login,name="login"),
  path("logout",views.logoutuser,name="logout"),
  path("logindetails",views.logindetails,name="logindetails"),
  path("delete/<id>",views.deleteData,name="delete"),
  path('update/<id>',views.updateData,name="updatetData"),
  path("adminn",views.adminn,name="admin"),
  path("contact",views.contact,name="contact"),
  path("about",views.about,name="about"),
  path('booking/<int:package_id>/', views.booking, name='booking'),
  path("profile",views.profile,name="profile"),
  path("packagesadd",views.packagesadd,name="packagesadd"),
  path('packagesviews',views.packagesviews,name='packagesview'),
  path("packagesdisplay",views.packagesdisplay,name="packagedisplay"),
  path('customize',views.customized,name="customize"),
  path("customdetails",views.customdetails,name="customdetails"),
  path("contactdetails",views.contactdetails,name="contactdetails"),
  path("bookingdetails",views.bookingdetails,name="bookingdetails"),
  path('edit_book/<id>/',views.edit_booking,name="edit_book"),
  path("cancel_booking/<int:id>/",views.cancelbook,name="cancel_booking"),
  path("cancel_custom/<int:id>/",views.cancelcustom,name="cancel_custom"),
  path('edit_custom/<id>/',views.edit_custom,name="edit_custom"),

 
  
]
