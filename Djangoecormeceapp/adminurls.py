from django.contrib import admin
from django.urls import path
from Djangoecormeceapp import views
from Djangoecormeceapp import AdminView


urlpatterns = [
    path('admin/',views.adminLogin, name="admin_login"),
    path('demo',views.demoPage),
    path('admin_login_process',views.adminLoginProcess, name="admin_login_process"),
    path('admin_logout_process',views.adminLogoutProcess, name="admin_logout_process"),
    # PAGE FOR ADMIN
    path('admin_home',AdminView.home,name="admin_home"),

    #categories
    path('category_list',AdminView.CategoriesListView.as_view(),name="category_list"),
    path('category_create',AdminView.CategoriesCreateView.as_view(),name="category_create"),
    path('category_update/<slug:pk>',AdminView.CategoriesUpdateView.as_view(),name="category_update"),


    #subcategories
    path('sub_category_list',AdminView.SubCategoriesListView.as_view(),name="sub_category_list"),
    path('sub_category_create',AdminView.SubCategoriesCreate.as_view(),name="sub_category_create"),
    path('sub_category_update/<slug:pk>',AdminView.SubCategoriesUpdate.as_view(),name="sub_category_update"),

    #MERCHANT USER
    path('merchant_create',AdminView.MerchantUserCreateView.as_view(),name="merchant_create"),
    path('merchant_list',AdminView.MerchantUserListView.as_view(),name="merchant_list"),
    path('merchant_update/<slug:pk>',AdminView.MerchantUserUpdateView.as_view(),name="merchant_update"),


     #PRODUCT  CREATE
    path('product_create',AdminView.ProductsCreateView.as_view(),name="product_create"),
    path('product_list',AdminView.ProductListView.as_view(),name="product_list"),
    path('product_update/<slug:pk>',AdminView.ProductsUpdateView.as_view(),name="product_update"),
    path('product_view',AdminView.ProductView.as_view(),name="product_view"),

    #this is the merchant url 
    path('merchant_home/',AdminView.merchant_home, name="merchant_home"),
    path('merchant_registration/',AdminView.merchant_registration, name="merchant_registration"),
    path('profile/',AdminView.profile, name="profile"),
    
]