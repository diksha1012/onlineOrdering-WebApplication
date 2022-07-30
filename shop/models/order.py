from django.db import models
from .product import Product
from .customer import Customer
import datetime
class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    # first_name=models.CharField(max_length=50,default="",blank=True)
    # last_name=models.CharField(max_length=50,default="")
    # email=models.EmailField () 
    date=models.DateField(default=datetime.datetime.today())
    status=models.BooleanField(default=False)

    def register(self):
        self.save()
    # def __str__(self):
    #      return self.product

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return  False
    
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order\
            .objects\
            .filter(customer=customer_id)\
            .order_by('-date')