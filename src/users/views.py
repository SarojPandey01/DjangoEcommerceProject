from django.shortcuts import render,redirect
from product.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import *
# Create your views here.

# def homepage(request):
#     product = Product.objcts.all()
#     # context = {
#     #     'product':product
#     # }
#     return render(request, 'users/index.html', {'product':product})

def homepage(request):
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'users/index.html', {'product':product} )

def productpage(request):
    product = Product.objects.all().order_by('-id')[:8]
    return render(request, 'users/products.html',{'product':product})

def product_detail(request,product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'users/productdetail.html', context)

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Account Created Successfully')
            return redirect('/register')
        else:
            messages.add_message(request, messages.ERROR,'Kindly Verify All The Fields')
            return render(request,'users/register.html',{'form':form})
    context={
        'form': UserCreationForm
    }
    return render(request,'users/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username = data['username'],password =data['password'])
            if user is not None:
                login(request,user)
                if user.is_staff:
                     return redirect('/admins')
                else:
                    return redirect('/')
            else:
                messages.add_message(request, messages.ERROR,'Kindly check the all fiekd')
                return render(request, 'users/login.html',{'form':form})
    context = {
        'form':LoginForm
    }
    return render(request, 'users/login.html',context)

def logout_user(request):
    logout(request)
    return redirect('/login')







