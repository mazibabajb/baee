from django.contrib import admin
from django.urls import path
from Djangoecormeceapp import views
from Djangoecormeceapp import AdminView


urlpatterns = [
    #this is the merchant url 
    path('merchant_home/',AdminView.merchant_home, name="merchant_home"),
    path('merchant_registration/',AdminView.merchant_registration, name="merchant_registration"),
    path('profile/',AdminView.profile, name="profile"),
    
]