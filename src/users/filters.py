import django_filters  
from product.models import *
from django_filters import CharFilter


class ProductFilter(django_filters.FilterSet):
    Product_name = CharFilter(field_name="product_name", lookup_expr="icontains")

    class Meta:    
        model = Product
        fields = ""
        exclude = ['product_price','image','category','description','created_at']
