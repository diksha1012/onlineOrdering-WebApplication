
from django.db.models.query_utils import select_related_descend
from shop.models.product import Product
# from django.http.response import HttpResponse
from django.shortcuts import render,redirect
# from django.http import JsonResponse
from shop.models.customer import Customer
from shop.models.category import Category
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
class Login(View):

       def get(self, request):
              return render(request,'login.html')
       def post(self,request):
              email = request.POST.get('email')
              password = request.POST.get('password')
              customer = Customer.get_customer_by_email(email)
              error_message=None
              if customer:
                     flag = check_password(password,customer.password)
                     if flag:
                            request.session['customer']=customer.id
                            # request.session['email']=customer.email
                            return redirect('homepage')
                     else:
                            error_message='Email or Password invalid!!'
              else:
                     error_message='Email or Password invalid!!'
              print(email,password)
              return render(request, 'login.html', {'error' : error_message})

def logout(request):
    request.session.clear()
    return redirect('login')