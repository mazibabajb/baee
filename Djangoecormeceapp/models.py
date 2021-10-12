from os import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from django.forms import ModelForm

# Create your models here.
class CustomUser(AbstractUser):
    user_type_choices = ((1, "Admin"), (2,"Staff"), (3,"Merchant"), (4,"Customer"), (5,"Afilliate"))
    user_type = models.CharField(max_length=255,choices=user_type_choices, default=1)


class AdminUser(models.Model):
    profile_pic = models.FileField(default="")
    auth_user_id =models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class StaffUser(models.Model):
    profile_pic = models.FileField(default="")
    auth_user_id =models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  


class MerchantUser(models.Model):
    profile_pic = models.FileField(default="")
    auth_user_id =models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    gst_details = models.CharField(max_length=255)
    address = models.TextField()
    is_added_by_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name


class CustomerUser(models.Model):
    profile_pic = models.FileField(default="")
    auth_user_id =models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  


class AffiliateUser(models.Model):
    profile_pic = models.FileField(default="")
    auth_user_id =models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)        
    

class Categories(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255) 
    description= models.TextField()
    thumbnail = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1) 
    is_active = models.IntegerField(default=1) 


    def get_absolute_url(self):
        return reverse("category_list")


    def __str__(self):
        return self.title


class SubCategories(models.Model):
    id=models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Categories,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255) 
    thumbnail = models.FileField()
    description= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)     

    def get_absolute_url(self):
        return reverse("sub_category_list")


    def __str__(self):
        return self.title

class IpAdress(models.Model):
    ip = models.CharField(max_length=100)

      
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    url_slug = models.CharField(max_length=255) 
    subcategories_id = models.ForeignKey(SubCategories,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255,blank=True)
    price = models.IntegerField(default=0)
    brand = models.CharField(max_length=255,blank=True)
    product_max_price = models.CharField(max_length=255,blank=True)
    product_discount_price = models.CharField(max_length=255,default=False)
    product_description = models.TextField()
    product_Long_description = models.TextField(blank=True)
    product_img = models.ImageField(upload_to='cars',default='default-car.png') 
    created_at = models.DateTimeField(auto_now_add=True)
    added_by_mechant = models.ForeignKey(MerchantUser,on_delete=models.CASCADE)
    is_onsale = models.BooleanField(default=False)
    is_hot = models.BooleanField(default=False)
    in_stock_total = models.IntegerField(default=1)
    views = models.ManyToManyField(IpAdress, blank=True, related_name="product_views")
    is_active = models.IntegerField(default=1) 


    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("product_detail",args=[self.id])


class Product_images(models.Model):
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    product_img = models.ImageField(upload_to='cars',default='default-car.png') 

   



class ProductMedia(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    media_type_choice = ((1,"Image"),(2,"Video"))
    media_type = models.CharField(max_length=255)
    media_content = models.FileField()
    product_img = models.ImageField(upload_to='cars',default='default-car.png') 
    is_active = models.IntegerField(default=1) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_id.product_name

class ProductTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    transaction_type_choices = ((1, "BUY"), (2,"SELL"))
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    transaction_product = models.IntegerField(default=1)
    transaction_type = models.CharField(choices=transaction_type_choices,max_length=255)
    transaction_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_id
    
   
class ProductDetails(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    title = models.CharField( max_length=100)
    title_detail = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1) 

    def __str__(self):
        return self.product_id


class ProductAbout(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1) 



class ProductTags(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    title = models.CharField(max_length=19)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1) 

    def __str__(self):
        return self.product_id

class ProductQuestons(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)  

    def __str__(self):
        return self.product_id   


class ProductReviews(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    rating = models.IntegerField(default="1")
    review_comment = models.TextField(max_length=200)
    ip =models.CharField(max_length=20, )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1) 

    def __str__(self):
        return self.product

class commentform(ModelForm):
        class Meta:
            model = ProductReviews
            fields = [ 'rating', 'review_comment']

    
        
        
class Search(models.Model):
    search = models.CharField(max_length=1000)

    def __str__(self):
        return self.search 
		       


class ProductReviewVoting(models.Model):
    id = models.AutoField(primary_key=True)
    product_review_id = models.ForeignKey(ProductReviews,on_delete=models.CASCADE)
    user_id_voting = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1) 

    def __str__(self):
        return self.product_review_id

class ProductVarient(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)




class ProductVarientItems(models.Model):
    id = models.AutoField(primary_key=True)
    product_varient_id = models.ForeignKey(ProductVarient,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)    


class CustomerOrders(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    purchase_price = models.CharField(max_length=255)
    coupon_code = models.CharField(max_length=255)
    discount_amt = models.CharField(max_length=255)
    product_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)       


class OderDeliveryStatus(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(CustomerOrders,on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    status_message= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now_add=True) 



class Contact_us(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    telephone = models.IntegerField(default=0)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Email(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email
         
 

    
@receiver(post_save,sender=CustomUser)     
def created_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminUser.objects.create(auth_user_id=instance)
        if instance.user_type==2:
            StaffUser.objects.create(auth_user_id=instance)
        if instance.user_type==3:
            MerchantUser.objects.create(auth_user_id=instance,company_name="",gst_details="",address="")
        if instance.user_type==4:
            CustomerUser.objects.create(auth_user_id=instance) 
        if instance.user_type==5:
            AffiliateUser.objects.create(auth_user_id=instance)    


@receiver(post_save,sender=CustomUser)     
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminuser.save()
    if instance.user_type==2:
        instance.staffuser.save()
    if instance.user_type==3:
        instance.merchantuser.save()
    if instance.user_type==4:
        instance.customeruser.save()  
    if instance.user_type==5:
        instance.affiliateuser.save()                   

    
