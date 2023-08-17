from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year_published = models.CharField(max_length=10)
    review = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title 
    
class User(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=11)
    wallet = models.FloatField(default=0)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    detail = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

class Order(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    qty = models.IntegerField()
    created_at = models.DateField(default=None, blank=True, null=True)
    updated_at = models.DateField(default=None, blank=True, null=True)
    CART = "CA"
    SHIPMANET = "SH"
    ORDER = "OR"
    STATUS = [
        (CART, "cart"),
        (ORDER, "order"),
        (SHIPMANET, "shipment"),
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default=CART,
    )
    def __str__(self):
        return self.product_id 
    

class Shipment(models.Model):
    track_no = models.CharField(max_length=100)
    address = models.IntegerField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    shipment_date = models.IntegerField()
    recieved_date = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()
    SUCCESS = "SU"
    PENDING = "PE"
    SHIPPING = "SH"
    STATUS = [
        (SUCCESS, "success"),
        (SHIPPING, "shipping"),
        (SUCCESS, "success"),
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default=PENDING,
    )
    def __str__(self):
        return self.product_id 
    
class ShipmentDetail(models.Model):
    order = models.IntegerField()
    shipment = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()
    def __str__(self):
        return self.order_id
    
class Admin(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=11)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Address(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    house_no = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    sub_district = models.CharField(max_length=50)
    provine = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    postcode = models.CharField(max_length=11)
    def __str__(self):
        return self.name