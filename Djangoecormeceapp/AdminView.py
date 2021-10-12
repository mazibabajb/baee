from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, View
from Djangoecormeceapp.models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.core.files.storage import FileSystemStorage
from django.contrib.messages.views import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q

@login_required(login_url="/admin")
def home(request):
    return render(request,"home.html")    


class CategoriesListView(ListView):     
    model = Categories
    template_name = "admintemplates/category_list.html"
    paginate_by=8
    
    
    def get_queryset(self):
        filter_val = self.request.GET.get("filter","")
        order_by=self.request.GET.get("orderby","id")
        if filter_val !="":
            cat=Categories.objects.filter(Q(title__contains=filter_val) |  Q(description__contains=filter_val)).order_by(order_by)
        else:
            cat=Categories.objects.all().order_by(order_by)    
        return cat

    def get_context_data(self, **kwargs): 
        context=super(CategoriesListView,self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get("filter","")
        context["orderby"]=self.request.GET.get("orderby","")
        context["all_table_fields"]=Categories._meta.get_fields()
        return context 
          


class CategoriesCreateView(SuccessMessageMixin,CreateView):
    model = Categories
    success_message = "category added"
    fields = "__all__"
    template_name =  "admintemplates/category_create.html"


class CategoriesUpdateView(SuccessMessageMixin,UpdateView):
    model = Categories
    success_message = "category updated"
    fields = "__all__"
    template_name =  "admintemplates/category_update.html"


class SubCategoriesListView(ListView):     
    model = SubCategories
    template_name = "admintemplates/sub_category_list.html"
    paginate_by=8
    
    
    def get_queryset(self):
        filter_val = self.request.GET.get("filter","")
        order_by=self.request.GET.get("orderby","id")
        if filter_val !="":
            cat=SubCategories.objects.filter(Q(title__contains=filter_val) |  Q(description__contains=filter_val)).order_by(order_by)
        else:
            cat=SubCategories.objects.all().order_by(order_by)    
        return cat

    def get_context_data(self, **kwargs): 
        context=super(SubCategoriesListView,self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get("filter","")
        context["orderby"]=self.request.GET.get("orderby","")
        context["all_table_fields"]=SubCategories._meta.get_fields()
        return context 

class SubCategoriesCreate(SuccessMessageMixin,CreateView):
    model = SubCategories
    success_message = "sub category added"
    fields = "__all__"
    template_name =  "admintemplates/sub_category_create.html"


class SubCategoriesUpdate(SuccessMessageMixin,UpdateView):
    model = SubCategories
    success_message = "sub category updated"
    fields = "__all__"
    template_name =  "admintemplates/sub_category_update.html" 


class MerchantUserListView(ListView):     
    model = MerchantUser
    template_name = "admintemplates/merchant_list.html"       
    paginate_by=8
    
    
    def get_queryset(self):
        filter_val = self.request.GET.get("filter","")
        order_by=self.request.GET.get("orderby","id")
        if filter_val !="":
            cat=MerchantUser.objects.filter(Q(title__contains=filter_val) |  Q(description__contains=filter_val)).order_by(order_by)
        else:
            cat=MerchantUser.objects.all().order_by(order_by)    
        return cat

    def get_context_data(self, **kwargs): 
        context=super(MerchantUserListView,self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get("filter","")
        context["orderby"]=self.request.GET.get("orderby","")
        context["all_table_fields"]=MerchantUser._meta.get_fields()
        return context 


class MerchantUserCreateView(SuccessMessageMixin,CreateView):
    model = CustomUser
    fields = ["first_name","last_name","email","username","password"]
    template_name =  "admintemplates/merchant_create.html"  


    def form_valid(self,form):

        #Saving Custom User Objects for mechant user
        user = form.save(commit=False)
        user.is_active = True
        user.user_type = 3
        user.set_password(form.cleaned_data["password"]) 
        user.save()


        #Saving Merchant User
        profile_pic=self.request.FILES["profile_pic"]
        fs=FileSystemStorage()
        filename = fs.save(profile_pic.name,profile_pic)
        profile_pic_url = fs.url(filename)


        user.merchantuser.profile_pic=profile_pic_url
        user.merchantuser.company_name = self.request.POST.get("company_name")
        user.merchantuser.gst_details = self.request.POST.get("gst_details")
        user.merchantuser.address = self.request.POST.get("address")
        is_added_by_admin = False

        if self.request.POST.get("is_added_by_admin")=="on":
            is_added_by_admin = True


        user.merchantuser.is_added_by_admin = is_added_by_admin
        user.save()
        messages.success(self.request,"Mechant Yser Created")
        return HttpResponseRedirect(reverse("merchant_list"))


class MerchantUserUpdateView(SuccessMessageMixin,UpdateView):
    model = CustomUser
    fields = ["first_name","last_name","email","username","password"]
    template_name =  "admintemplates/merchant_update.html"  


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        merchantuser = MerchantUser.objects.get(auth_user_id=self.object.pk)
        context["merchantuser"]=merchantuser
        return context


    def form_valid(self,form):

        #Saving Custom User Objects for mechant user
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"]) 
        user.save()


        #Saving Merchant User
        merchantuser = MerchantUser.objects.get(auth_user_id=user.id)
        if self.request.FILES.get("profile_pic", False):
            profile_pic=self.request.FILES["profile_pic"]
            fs=FileSystemStorage()
            filename = fs.save(profile_pic.name,profile_pic)
            profile_pic_url = fs.url(filename)
            merchantuser.profile_pic=profile_pic_url


        merchantuser.company_name = self.request.POST.get("company_name")
        merchantuser.gst_details = self.request.POST.get("gst_details")
        merchantuser.address = self.request.POST.get("address")
        is_added_by_admin = False

        if self.request.POST.get("is_added_by_admin")=="on":
            is_added_by_admin = True


        merchantuser.is_added_by_admin = is_added_by_admin
        merchantuser.save()
        messages.success(self.request,"Mechant Yser Updated")
        return HttpResponseRedirect(reverse("merchant_list"))


class ProductListView(ListView):     
    model = Categories
    template_name = "admintemplates/category_list.html"
    paginate_by=8
    
    
    def get_queryset(self):
        filter_val = self.request.GET.get("filter","")
        order_by=self.request.GET.get("orderby","id")
        if filter_val !="":
            cat=Products.objects.filter(Q(title__contains=filter_val) |  Q(description__contains=filter_val)).order_by(order_by)
        else:
            cat=Products.objects.all().order_by(order_by)    
        return cat

    def get_context_data(self, **kwargs): 
        context=super(ProductListView,self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get("filter","")
        context["orderby"]=self.request.GET.get("orderby","")
        context["all_table_fields"]=Products._meta.get_fields()
        return context 


class ProductsCreateView(SuccessMessageMixin,CreateView):
    model = Products
    success_message = "category added"
    fields = "__all__"
    template_name =  "admintemplates/category_create.html"


class ProductsUpdateView(SuccessMessageMixin,UpdateView):
    model = Products
    success_message = "category updated"
    fields = "__all__"
    template_name =  "admintemplates/category_update.html"


class ProductView(View):
    def get(self,request,*args,**kwargs):
        categories=Categories.objects.filter(is_active=1)
        categories_list=[]
        for category in categories:
            sub_category=SubCategories.objects.filter(is_active=1,category_id=category.id)
            categories_list.append({"category":category,"sub_category":sub_category  })

        merchant_users=MerchantUser.objects.filter(auth_user_id__is_active=True)    
            
        return render(request,"admintemplates/product_create.html",{"categories":categories_list, "merchant_users":merchant_users })


        def post(self,request,*args,**kwargs):
            return HttpResponse("form saved of Product")


#this is th mechant home  views

@login_required(login_url="/admin")
def merchant_home(request):
    return render(request,"merchant_templates/merchant_home.html")

def merchant_registration(request):
    return render(request,"merchant_templates/merchant_registration.html")  

def profile(request):
    return render(request,"merchant_templates/profile.html")                   


#affiliate views
@login_required(login_url="/admin")
def affilliate_home(request):
    return render(request,"affilliate_templates/affilliate_home.html")    