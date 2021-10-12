from django.contrib import admin
from.models import*
from Djangoecormeceapp.forms import *

# Register your models here.

class ProductCreateForm(admin.ModelAdmin):
    list_display = ['url_slug','product_name', 'brand', 'price','subcategories_id','added_by_mechant','in_stock_total']
admin.site.register(Products, ProductCreateForm)


class SubCategoryCreateForm(admin.ModelAdmin):
    list_display = ['category_id','title', 'url_slug']	
admin.site.register(SubCategories, SubCategoryCreateForm)    


class CategoryCreateForm(admin.ModelAdmin):  
    list_display =  ['title', 'url_slug'] 
admin.site.register(Categories, CategoryCreateForm)
admin.site.register(Search)
admin.site.register(Email)
admin.site.register(Contact_us)
admin.site.register(ProductMedia)
admin.site.register(ProductTransaction)
admin.site.register(ProductDetails)
admin.site.register(ProductAbout)
admin.site.register(ProductTags)
admin.site.register(ProductQuestons)
admin.site.register(ProductReviews)
admin.site.register(ProductReviewVoting)
admin.site.register(ProductVarient)
admin.site.register(ProductVarientItems)
admin.site.register(OderDeliveryStatus)
admin.site.register(CustomerOrders)
admin.site.register(CustomUser)
admin.site.register(AdminUser)
admin.site.register(MerchantUser)
admin.site.register(Product_images)
admin.site.register(IpAdress)


