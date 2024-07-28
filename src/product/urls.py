from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("home/", views.home, name="home"),
    path("addproduct/", views.add_product, name="addproduct"),
    path("addcategory/", views.add_category, name="productcategory"),
    path('productlist/', views.productlist, name="productlist"),
    path('updateproduct/<int:product_id>',views.update_product, name="updateproduct"),
    path('deleteproduct/<int:product_id>', views.delete_product, name="deleteproduct" ),
    path('categorylist/', views.categorylist, name="categorylist"),
    path("updatecategory/<int:category_id>", views.update_category, name="updatecategory"),
    path('deletecategory/<int:category_id>',views.delete_category, name="deletecategory"),
    path('orderlist/',views.orderlist,name='orderlist')

]
