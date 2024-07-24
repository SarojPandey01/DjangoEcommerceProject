from django.db import models

from product.models import *
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    PAYMENT = (
        ('Cash on Delivery', 'Cash on Delivery'),
        ('Esewa','Esewa')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    payment_method = models.CharField(max_length=200, choices=PAYMENT)
    payment_status = models.BooleanField(default=False)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=200)
    

