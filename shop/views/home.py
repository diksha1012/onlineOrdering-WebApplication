from django.db.models.query_utils import select_related_descend
from shop.models.product import Product
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
# from django.http import JsonResponse
from shop.models.customer import Customer
from shop.models.category import Category
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

# print(make_password('1234'))
# Create your views here.
 
class Index(View):
    def post(self, request):
        product=request.POST.get('product')
        remove = request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:

                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        
        request.session['cart']=cart
        print('cart', request.session['cart'])
        return redirect('homepage')
   
   
   
   
    def get(self,request):
       cart=request.session.get('cart')
       if not cart:
           request.session['cart'] ={}
       products=None
    #    request.session.get('cart').clear()
       categories = Category.get_all_categories()
       categoryId=request.GET.get('category')
       if categoryId:
              products= Product.get_products_by_all_categoryId(categoryId)
       else:
              products=Product.get_all_products();
       data = {}
       data['products']=products
       data['categories']=categories
       # print(products)
       # return render(request,'shop/base.html') 
       print('you are: ',request.session.get('email'))
       return render(request,'index.html', data)
