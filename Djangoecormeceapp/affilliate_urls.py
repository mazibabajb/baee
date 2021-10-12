from django.contrib import admin
from django.urls import path
from Djangoecormeceapp import views
from Djangoecormeceapp import AdminView


urlpatterns = [

    path('affilliate_home/',AdminView.affilliate_home, name="affilliate_home"),
  
    
]