from django.db import models
from django.db.models.fields import EmailField

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone= models.CharField(max_length=15,default="")
    email=models.EmailField () 
    password=models.CharField(max_length=50,default="")

    def register(self):
        self.save()
        
    
    def __str__(self):
         return self.first_name

    @staticmethod
    def get_customer_by_email(email):
        try:
              return Customer.objects.get(email= email)
        except:
            return False

    


            
    
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True


        return False