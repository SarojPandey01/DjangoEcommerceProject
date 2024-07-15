from django.forms import ModelForm
from . models import *


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class ProductCategory(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        

    
  