from django.shortcuts import render,redirect
from users.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from users.auth import admin_only



# Create your views here.
def admin_page(request):
    return render(request,'admins/admin.html')

@login_required
@admin_only
def user_list(request):
    user = User.objects.all()
    context = {
        'user':user
    }
    return render(request,'admins/userlist.html', context)

