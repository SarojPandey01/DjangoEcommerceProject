from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True, null=True)
    
    
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=200, null=False)
    product_price = models.FloatField( null=False)
    quantity = models.IntegerField(null=False)
    description = models.TextField()
    image = models.FileField(upload_to='static/updates', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name



