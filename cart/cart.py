from decimal import Decimal
from django.conf import settings
from Djangoecormeceapp.models import Products


class Cart(object):
    def __init__(self,request):
        """initialisins cart session id"""
        self.session=request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart = cart


    def add(self,products,quantity=1,override_quantity=False):
        products_id = str(products.id)
        if products_id not in self.cart:
            self.cart[products_id]={'quantity':0, 'price':str(products.price)}

        if overrride_quantity:
            self.cart[products_id]['quantity']=quantity
        else:
            self.cart[products_id]['quantity'] +=quantity
        self.save()    

    def save(self):
        self.session.modified = True


    def remove(self,products):
        products_id = str(products.id)
        if products_id in self.cart:
            del self.cart[products_id]
            self.save()


    def __iter__(self):
        products_id= self.cart.keys()
        products = Products.objects.filter(id__in=products_id)


        cart = self.cart.copy()
        for products in products:
            cart[str(products.id)]['product'] = products

        for item in cart.values():
            item['price']=Decimal(item['price']) 
            item['total_price']=item['price'] * item['quantity'] 
            yield item


        def __len__(self):
            return sum(item['quantity'] for item in self.cart.values())

        def get_total_price(self):
            return sum(Decimal(item['price'] * item['quantity']) for item in self.cart.values())                             

        def clear(self):
            del self.session[settings.CART_SESSION_ID]
            self.save()
