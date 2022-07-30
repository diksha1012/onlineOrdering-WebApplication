from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from shop.models.customer import Customer
from django.views import View

from shop.models.product import Product
from shop.models.order import Order
# from store.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        order=orders.reverse()
        return render(request , 'orders.html' , {'orders': orders} )