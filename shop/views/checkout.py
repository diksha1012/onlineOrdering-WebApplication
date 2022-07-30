from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from shop.models.customer import Customer
from django.views import  View
from shop.models.product import  Product
from shop.models.order import  Order

class CheckOut(View):
    def post(self , request):
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_products_by_id(list(cart.keys()))
        print(phone,customer,cart,products)

        
        for product in products:
            print(cart.get(str(product.id)))
            order=Order(customer=Customer(id=customer),
                        product=product,
                        price=product.price,
                        quantity=cart.get(str(product.id)),
                        # phone=phone
                        )
            order.save()
        request.session['cart']={}

        return redirect('cart')