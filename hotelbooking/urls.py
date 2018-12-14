"""hotelbooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView
from akbarhotel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.openHomePage),
    path('openHomePage/',views.openHomePage),

    path('openServicesPage/',views.openServicesPage),

    path('openUserLogin/',views.openUserLogin),
    path('openSignUpPage/',views.openSignUpPage),
    path('registerUser/',views.registerUser),
    path('loginUser/',views.loginUser),


    path('openUserHomePage/',views.openUserHomePage),
    path('openBookingPage/',views.openBookingPage),
    path('openPayment/',views.openPayment),
    path('openPreview/',views.openPreview),


    path('openContactPage/',views.openContactpage),
    path('ContactPage/', views.ContactPage),

    path('openCancelPage/',views.openCancelPage),
    path('CancelPage/',views.CancelPage)





]
