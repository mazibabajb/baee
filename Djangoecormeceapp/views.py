from django.forms.forms import Form
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse,HttpResponseRedirect, request
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import DetailView
from Djangoecormeceapp.models import Contact_us, ProductMedia, Products, Categories,SubCategories,commentform,ProductReviews,Email, Search
from blog.models import Post
from django.core.paginator import Paginator , EmptyPage
from cart.forms import CartAddProductForm
from django.contrib import messages




# Create your views here.


def demoPage(request):
    return HttpResponse("demo Page")


def emailsubscription(request):
    if request.method == 'POST':
        email_sub = Email()
        email = request.POST.get('email')
        email_sub.email = email
        email_sub.save()
        messages.success(request, 'Thank you for subscribing to')
    return render(request,"front_end_templates/index.html")    

        

    

def searchbar(request):
    if request.method == 'GET':
        seacrh_term = Search()
        search = request.GET.get('search')
        products = Products.objects.all().filter(product_name = search)
        seacrh_term.search = search
        seacrh_term.save()
    return render(request,"front_end_templates/search.html",{'products':products})

       

def home(request):
    is_trending = Post.objects.filter(is_trending = True).order_by('-id')[:4]
    is_onsale = Products.objects.filter(is_onsale = True).order_by('-id')[:4]
    is_hot = Products.objects.filter(is_hot = True).order_by('-id')[:4]


    context = {
        'is_trending': is_trending,
        'is_hot': is_hot,
        'is_onsale': is_onsale
    }
    return render(request,"front_end_templates/index.html",context)



def home_product_detail(request, id):
    products = Products.objects.get(id=id)
    related_products = Products.objects.filter(subcategories_id = products.subcategories_id).exclude(id=id)[:2]
    context = {
		'products': products,
        'related_product':related_products,
		
	}
    return render(request, "front_end_templates/products_detail.html",context)



def Product_view(request):
	productCategory = request.GET.get('productCategory')
	if productCategory == None:
		products = Products.objects.all()
	else:
		products = Products.objects.filter(subcategories_id__title=productCategory)	
        	
	productCategories = SubCategories.objects.all()
	page_num = request.GET.get('page', 1)
	p = Paginator(products, 7)

	try:
		page = p.page(page_num)

	except EmptyPage:
		page = p.page(1)
    
	context = {	'products':page ,
				'productCategories':productCategories,
				}
	return render(request, 'front_end_templates/products_list_view.html',context)


def get_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def product_detail(request, id):
    products = Products.objects.get(id=id)
    product_images = ProductMedia.objects.all()
    related_products = Products.objects.filter(subcategories_id = products.subcategories_id).exclude(id=id)[:2]
    cart_product_form = CartAddProductForm()
    context = {
		'products': products,
        'cart_product_form':cart_product_form,
        'related_products': related_products,
        'product_images': product_images,
		
	}
    return render(request, "front_end_templates/products_detail.html",context)

def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    #return HttpResponse(url)
    if request.method == 'POST':
        form = commentform(request.POST)
        if form.is_valid():
            data = ProductReviews()
            data.review_comment = form.cleaned_data['review_comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product =id
            currenr_user = request.user
            data.user=currenr_user.id
            data.save()
            messages.success(request, 'your review has been sent thank you for your intrest')
            return HttpResponseRedirect(url)
            
    return HttpResponseRedirect(url)
    

class ProductListView(ListView):     
    model = Products
    template_name = "front_end_templates/products_list_view.html"
    paginate_by=2
    
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

	 

class ProductDetailView(DetailView):
    model = Products
    template_name = "front_end_templates/products_detail.html"



	 
    

def AboutUs(request):
    return render(request,"front_end_templates/about-us.html")

def Faqs(request):
    return render(request,"front_end_templates/faqs.html")


def Payments(request):
    return render(request,"front_end_templates/payments.html") 

def Deliveries(request):
    return render(request,"front_end_templates/deliveries.html")    

def Contact_Us(request):
    if request.method == 'POST':
        contact = Contact_us()
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        comment = request.POST.get('comment')
        contact.name = name
        contact.email = email
        contact.telephone = telephone
        contact.comment= comment
        contact.save()
        messages.success(request, 'your review has been sent thank you for your intrest')
    return render(request,"front_end_templates/contact-us.html")          
          
           

	
def BlogList(request):
    return render(request,"front_end_templates/blog_list.html") 


def BlogDetail(request):
    return render(request,"front_end_templates/blog_detail.html") 



def adminLogin(request):
    return render(request,"admintemplates/signin.html")   


def adminLoginProcess(request):
    username=request.POST.get("username")  
    password=request.POST.get("password") 


    user=authenticate(request=request,username=username,password=password)  
    if user is not None:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("admin_home"))
    else:
        messages.error(request,"Error in Login! Invalid login details")
        return HttpResponseRedirect(reverse("admin_login"))


def adminLogoutProcess(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return HttpResponseRedirect(reverse("home"))
