from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.


class customer(models.Model):

    user=models.OneToOneField(User,on_delete=CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100,blank=False,null=False)
    email=models.CharField(max_length=200,blank=True,null=True)

    def __str__(self) :
        return self.name



class product(models.Model):
   
    name=models.CharField(max_length=100,blank=False,null=False)
    price=models.FloatField()
    digital=models.BooleanField(default=False)
    image=models.ImageField(null=True,blank=True)
    

    def __str__(self) :
        return self.name


    @property
    def imageUrl(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

class Order(models.Model):
   
    customer=models.ForeignKey(customer,on_delete=SET_NULL,null=True, blank=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    transaction_id=models.CharField(max_length=100,blank=False,null=False)
    complete=models.BooleanField(default=False,blank=False,null=True)

    def __str__(self) :
        return str(self.id)



    @property
    def get_cart_total(self):
        orderitem = self.orderitems_set.all()
        total = sum([item.get_total for item in orderitem])
        return total 

    @property
    def get_cart_items(self):
        orderitem = self.orderitems_set.all()
        total = sum([item.quantity for item in orderitem])
        return total 




    


class orderitems(models.Model):
   
    product=models.ForeignKey(product,on_delete=SET_NULL,null=True,blank=False)
    order=models.ForeignKey(Order,on_delete=SET_NULL,null=True,blank=False)
    quantity=models.IntegerField(default=0,blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)



    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class shippingAddress(models.Model):
   
    customer=models.ForeignKey(customer,on_delete=SET_NULL,null=True,blank=False)
    order=models.ForeignKey(Order,on_delete=SET_NULL,null=True,blank=False)
    address=models.CharField(max_length=100,blank=False,null=False)
    city=models.CharField(max_length=100,blank=False,null=False)
    state=models.CharField(max_length=100,blank=False,null=False)
    zipcode=models.CharField(max_length=100,blank=False,null=False)
    date_added=models.DateTimeField(auto_now_add=True)


    def __str__(self) :
        return str(self.id)