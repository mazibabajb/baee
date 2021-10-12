from django.contrib import admin
from django.urls import path
from Djangoecormeceapp import views
from Djangoecormeceapp import AdminView


urlpatterns = [
    path('',views.home, name="home"),
    path('productlist/',views.ProductListView.as_view(), name="productlist"),
    path('product_detail/<int:id>/',views.product_detail, name="product_detail"),
    path('home_product_detail/<int:id>/',views.home_product_detail, name ='home_product_detail'),
    path('contact_us/',views.Contact_Us, name="contact_us"),
    path('emailsubscription/',views.emailsubscription, name="emailsubscription"),
    path('addcomment/<int:id>/',views.addcomment, name="addcomment"),
    path('about_us/',views.AboutUs, name="about_us"),
    path('payments/',views.Payments, name="payments"),
    path('faqs/',views.Faqs, name="faqs"),
    path('deliveries/',views.Deliveries, name="deliveries"),
    path('product_list_view/',views.Product_view, name="product_list_view"),
    path('searchbar/',views.searchbar, name="searchbar"),
     
]