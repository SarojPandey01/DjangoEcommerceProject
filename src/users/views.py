from django.shortcuts import render,redirect
from product.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import *
from . models import *
from django.contrib.auth.decorators import login_required
from . filters import *
from django.core.paginator import Paginator


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
    user = request.user
    items = Cart.objects.filter(user=user)
    product = Product.objects.all().order_by('-id')
    product_filter = ProductFilter(request.GET, queryset=product)
    product_final = product_filter.qs

    pages = Paginator(product_final,2)
    pagenumber = request.GET.get('page')
    # pagenumber = request.GET.get('page') le url bata page number linxa 
    new_product = pages.get_page(pagenumber)

    context = {
        'product': new_product,
        'product_filter': product_filter,
        'items':items
    }
    return render(request, 'users/products.html',context)

def product_detail(request,product_id):
    user = request.user.id
    items = Cart.objects.filter(user=user)
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
        'items':items
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

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id = product_id)
    user = request.user

    check_item_presence = Cart.objects.filter(user=user, product=product)
    if check_item_presence:
        messages.add_message(request,messages.ERROR,f'{product.product_name} is already presrnt in cart')
        return redirect(f'/productdetail/{product_id}')
    else:
        Cart.objects.create(user=user,product=product)
        if Cart:
            messages.add_message(request,messages.SUCCESS,'Product added successfully in cart')
            return redirect('/cart')
        else:
            messages.add_message(request,messages.ERROR,'Error while addeing in cart')
           

@login_required
def viewcart(request):
    user = request.user.id
    items = Cart.objects.filter(user=user)
    context = {
        'items':  items

    }
    return render(request,'users/cart.html',context)

@login_required
def deletecart(request,cart_id):
    item = Cart.objects.get(id = cart_id)
    item.delete()
    messages.add_message(request, messages.ERROR,"Product removed from the cart")
    return redirect('/cart')






@login_required
def order(request, product_id, cart_id):
    user = request.user
    product = Product.objects.get(id= product_id)
    cart = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        quantity = request.POST.get('quantity')
        price = product.product_price
        total_price = int(quantity)*int(price)
        contact_no = request.POST.get('contact_no')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        order = Order.objects.create(
            user = user,
            product =product,
            quantity = quantity,
            total_price = total_price,
            contact_no = contact_no,
            address = address ,
            payment_method = payment_method
        )
        if order.payment_method == 'Cash on Delivery':
            cart.delete()
            messages.add_message(request,messages.SUCCESS,'Ypur order has been succussfully ordered')
            return redirect('/myorder')
    context = {
        'form':OrderForm
    }
    return render(request,'users/order.html',context)




@login_required
def myorder(request):
    user = request.user
    order = Order.objects.filter(user= user)
    context = {
        'order':order
    }
    return render(request,'users/myorder.html',context)






