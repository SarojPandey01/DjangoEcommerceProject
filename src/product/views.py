from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def index(request):
    return HttpResponse("Welcome to django project")


def home(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request,'products/index.html',context)

def productlist(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request,'products/allproducts.html',context)


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Add Product Successfully')
            return redirect('/product/addproduct')
        else:
            messages.add_message(request, messages.ERROR,'Kindly verify all fields')
            return render(request, 'products/addproduct.html', {"form":form})
    context = {
        'form': ProductForm
    }
    return render(request,'products/addproduct.html',context)


@login_required
def add_category(request):
    if request.method == "POST":
        cat = ProductCategory(request.POST)
        if cat.is_valid():
            cat.save()
            return redirect('/product/addcategory')
        else:
            return render(request, 'products/productcategory.html',{"form":cat})
    context = {
            'form':ProductCategory
        }
    return render(request,'products/productcategory.html',context)



@login_required
def update_product(request,product_id):
    instance = Product.objects.get(id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Product updated successfuly')
            return redirect('/product/productlist')
        else:
            messages.add_message(request,messages.SUCCESS,'kindly verify all the fields')
            return render(request, '/products/updateproduct.html',{'form':form})
    context = {
        'form':ProductForm(instance=instance)
    }
    return render(request, 'products/updateproduct.html', context)


@login_required
def delete_product(request, product_id):
    isinstance= Product.objects.get(id=product_id)
    isinstance.delete()
    messages.add_message(request,messages.SUCCESS,'Product deleted successfully')
    return redirect('/product/productlist')


def categorylist(request):
    category = Category.objects.all()
    context={
        "category":category
    }
    return render(request,'products/categorylist.html',context)



@login_required
def update_category(request,category_id):
    instance = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = ProductCategory(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Category updated successfuly')
            return redirect('/product/categorylist')
        else:
            messages.add_message(request,messages.SUCCESS,'kindly verify all the fields')
            return render(request, '/products/updatecategory.html',{'form':form})
    context = {
        'form':ProductCategory(instance=instance)
    }
    return render(request, 'products/updatecategory.html', context)



@login_required
def delete_category(request, category_id):
    isinstance= Category.objects.get(id=category_id)
    isinstance.delete()
    messages.add_message(request,messages.SUCCESS,'Category deleted successfully')
    return redirect('/product/categorylist')



