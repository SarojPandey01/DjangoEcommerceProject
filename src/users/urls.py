from  django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('products/', views.productpage, name='products'),
    path('productdetail/<int:product_id>', views.product_detail, name='productdetail'),
    path('register/',views.user_register,name='register')
  

]
