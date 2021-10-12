from django import forms
from django.db.models.fields import TextField
from .models import *

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields =  ['url_slug','product_name', 'brand', 'price','subcategories_id','added_by_mechant','in_stock_total']


class SubCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = SubCategories
        fields =  ['category_id','title', 'url_slug']		


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields =  ['title', 'url_slug']


	
			